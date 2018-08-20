package cn.sibat.gongAn.apps

import java.sql.Date
import java.text.SimpleDateFormat
import java.util.Properties

import org.apache.spark.sql.{DataFrame, Row, SparkSession}
import org.apache.spark.sql.functions._

import scala.collection.mutable.ArrayBuffer

/**
  * 读取一周的公安设备数据，进行布吉站质量监督
  * 数据在统计前进行去重并去除国标码字段为空的数据
  * Created by wing on 2018/6/18.
  */
object Monitoring {

    /**
      * 从数据库中读取静态信息表
      * @param sparkSession spark
      * @param url utl
      * @param table table
      * @param user user
      * @param password password
      * @return staticTable
      */
    def readFromDB(sparkSession: SparkSession, url: String, table: String, user: String, password: String, driver: String): DataFrame = {
      val prop = new Properties()
      prop.setProperty("user", user)
      prop.setProperty("password", password)
      prop.setProperty("driver", driver) //com.mysql.jdbc.Driver org.postgresql.Driver

      val staticTable = sparkSession.read.jdbc(url, table, prop)
      staticTable
    }

    /**
      * 计算总体布吉每天每个设备的数据质量（服务器接收时间）
      * a)	每个设备15分钟粒度数据接收数；
      * @param df 原始数据
      * @return 总体质量的报表
      */
    def general(df: DataFrame): DataFrame = {

        import df.sparkSession.implicits._

        val result = df.groupByKey(row => row.getAs[String]("deviceType") + " " + row.getAs[String]("serverReceiveTime").split(" ")(0) + " " + row.getAs[String]("gbNo"))
            .mapGroups((key, iter) => {
                val deviceType = key.split(" ")(0)
                val date = key.split(" ")(1)
                val gbNo = key.split(" ")(2)
                val records = iter.toArray
                val count = records.length //全天布吉站上每个设备接收数据的总条数

                val timeArray = new Array[Int](96)//每15分钟产生的数据条数组成的长度为96的数组
                records.groupBy(row => {
                  val serverReceiveTime = row.getAs[String]("serverReceiveTime")
                  val sdf1 = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss")
                  val timeStamp = sdf1.parse(serverReceiveTime).getTime

                  val sdf2 = new SimpleDateFormat("yyyy-MM-dd")
                  val dateStamp = sdf2.parse(date).getTime

                  val time = timeStamp - dateStamp
                  val timePeriod = time / 1000 / 60 / 15 //会自动向下取整

                  timePeriod.toInt
                }).foreach(tuple => {
                    val period = tuple._1
                    val periodCount = tuple._2.length
                    try {
                      timeArray(period) = periodCount
                    } catch {
                      case _: java.lang.ArrayIndexOutOfBoundsException => println(period + " I am here")
                    }

                })

              (date, deviceType, gbNo, count, timeArray)
            }
            ).toDF("date", "deviceType",  "gbNo", "count", "timeArray")
        result
    }

    /**
      * 计算布吉站设备相邻数据产生的间隔（根据设备捕捉时间，其中任子行没有数据捕捉时间）
      * a)	全天单个设备的平均间隔。
        b)	所有设备根据数据条数各间隔时间内有多少条数据（0~5s,5~10s,10~30s,30~60s,60~120s,120~180s,180~240s,240~300s,大于300s），输出不同间隔内的数据所占比例。
        c)	所有设备最小，最大，平均发送间隔
      * @param df 原始数据
      * @return 数据间隔统计报表
      */
    def timeSpan(df: DataFrame): DataFrame = {

        import df.sparkSession.implicits._
        val result = df.groupByKey(row => row.getAs[String]("time").split(" ")(0) + " " + row.getAs("gbNo"))
            .mapGroups((key, iter) => {
                val date = key.split(" ")(0)
                val gbNo = key.split(" ")(1)
                val records = iter.toArray.sortBy(row => row.getAs[Long]("timestamp"))

                var spanForDay = 0.0 //全天总时间间隔
                var countForDay = 1.0 //全天数据条数

                var countLessThan5 = 0.0 //0~5s内的数据条数
                var countLessThan10 = 0.0
                var countLessThan30 = 0.0
                var countLessThan60 = 0.0
                var countLessThan120 = 0.0
                var countLessThan180 = 0.0
                var countLessThan240 = 0.0
                var countLessThan300 = 0.0
                var countMoreThan300 = 0.0 //大于300秒的数据条数

                var firstTimestamp = records(0).getAs[Long]("timestamp")
                var minTimeSpan = Long.MaxValue
                var maxTimeSpan = Long.MinValue

                records.slice(1, records.length).foreach(row => {
                    val secondTimestamp = row.getAs[Long]("timestamp")
                    val span = secondTimestamp - firstTimestamp
                    if (span > maxTimeSpan) maxTimeSpan = span
                    if (span < minTimeSpan) minTimeSpan = span

                    spanForDay += span
                    countForDay += 1

                    if (span >=0 && span < 5) countLessThan5 += 1
                    else if (span >= 5 && span < 10) countLessThan10 += 1
                    else if (span >= 10 && span < 30) countLessThan30 += 1
                    else if (span >= 30 && span < 60) countLessThan60 += 1
                    else if (span >= 40 && span < 120) countLessThan120 += 1
                    else if (span >= 50 && span < 180) countLessThan180 += 1
                    else if (span >= 60 && span < 240) countLessThan240 += 1
                    else if (span >= 240 && span < 300) countLessThan300 += 1
                    else if (span >= 300) countMoreThan300 += 1

                    firstTimestamp = secondTimestamp
                })
                (gbNo, spanForDay / countForDay, minTimeSpan, maxTimeSpan, countLessThan5 / countForDay, countLessThan10 / countForDay, countLessThan30 / countForDay, countLessThan60 / countForDay, countLessThan120 / countForDay, countLessThan180 / countForDay, countLessThan240 / countForDay, countLessThan300 / countForDay, countMoreThan300 / countForDay)
            }).toDF("gbNo", "avgSpan", "minTimeSpan", "maxTimeSpan", "ratio_countLessThan5", "ratio_countLessThan10", "ratio_countLessThan30", "ratio_countLessThan60", "ratio_countLessThan120", "ratio_countLessThan180", "ratio_countLessThan240", "ratio_countLessThan300", "ratio_countMoreThan300")
        result
    }

    /**
      * 计算时间延迟
      * a)	所有设备的平均延迟。
        b)	所有设备数据各延迟时间内有多少条数据（小于0s，0~1s，1~2s，2~3s，3~4s，4~5s，5~10s，10~30s，30~60s，60~120，120~180，180~240，240~300，大于300s），以及对应的数据所占比例。
        c)	所有设备最小，最大，平均延迟时间
      * @param df 原始数据
      * @return
      */
    def timeDelay(df: DataFrame): DataFrame = {

        import df.sparkSession.implicits._
        df.groupByKey(row => row.getAs[String]("time").split(" ")(0) + " " + row.getAs("gbNo"))
            .mapGroups((key, iter) => {
                val date = key.split(" ")(0)
                val gbNo = key.split(" ")(1)

                var count = 0.0
                var delayCount = 0.0 //设备延迟数据量
                var allDelaySeconds = 0.0 //设备全天延迟时间

                var minDelaySeconds = Long.MaxValue
                var maxDelaySeconds = Long.MinValue

                var delayLess0Seconds = 0.0 //延迟时间为负值的数据量
                var delayLess1Seconds = 0.0
                var delayLess2Seconds = 0.0
                var delayLess3Seconds = 0.0
                var delayLess4Seconds = 0.0
                var delayLess5Seconds = 0.0
                var delayLess10Seconds = 0.0
                var delayLess30Seconds = 0.0
                var delayLess60Seconds = 0.0
                var delayLess120Seconds = 0.0
                var delayLess180Seconds = 0.0
                var delayLess240Seconds = 0.0
                var delayLess300Seconds = 0.0
                var delayMore300Seconds = 0.0

                iter.foreach(row => {
                    count += 1
                    val serverReceiveTimestamp = row.getAs[Long]("serverReceiveTimestamp")
                    val timestamp = row.getAs[Long]("timestamp")
                    val timeDiff = serverReceiveTimestamp - timestamp
                    if (timeDiff > maxDelaySeconds) maxDelaySeconds = timeDiff
                    if (timeDiff < minDelaySeconds) minDelaySeconds = timeDiff

                    if (timeDiff != 0) {
                        delayCount += 1
                        allDelaySeconds += timeDiff
                        if (timeDiff < 0) delayLess0Seconds += 1
                        else if (timeDiff > 0 && timeDiff <= 1) delayLess1Seconds += 1
                        else if (timeDiff > 1 && timeDiff <= 2) delayLess2Seconds += 1
                        else if (timeDiff > 2 && timeDiff <= 3) delayLess3Seconds += 1
                        else if (timeDiff > 3 && timeDiff <= 4) delayLess4Seconds += 1
                        else if (timeDiff > 4 && timeDiff <= 5) delayLess5Seconds += 1
                        else if (timeDiff > 5 && timeDiff <= 10) delayLess10Seconds += 1
                        else if (timeDiff > 10 && timeDiff <= 30) delayLess30Seconds += 1
                        else if (timeDiff > 30 && timeDiff <= 60) delayLess60Seconds += 1
                        else if (timeDiff > 60 && timeDiff <= 120) delayLess120Seconds += 1
                        else if (timeDiff > 120 && timeDiff <= 180) delayLess180Seconds += 1
                        else if (timeDiff > 180 && timeDiff <= 240) delayLess240Seconds += 1
                        else if (timeDiff > 240 && timeDiff <= 300) delayLess300Seconds += 1
                        else if (timeDiff > 300) delayMore300Seconds += 1

                    }
                })

                (gbNo, delayCount/ count, allDelaySeconds / delayCount, minDelaySeconds, maxDelaySeconds, delayLess0Seconds / count, delayLess1Seconds / count, delayLess2Seconds / count, delayLess3Seconds / count, delayLess4Seconds / count, delayLess5Seconds / count, delayLess10Seconds / count, delayLess30Seconds / count, delayLess60Seconds / count, delayLess120Seconds / count, delayLess180Seconds / count, delayLess240Seconds / count, delayLess300Seconds / count, delayMore300Seconds / count)
            }).toDF("gbNo", "delayRatio", "avgDelaySeconds", "minDelaySeconds", "maxDelaySeconds", "ratio_delayLess0Seconds", "ratio_delayLess1Seconds", "ratio_delayLess2Seconds", "ratio_delayLess3Seconds", "ratio_delayLess4Seconds", "ratio_delayLess5Seconds", "ratio_delayLess10Seconds ", "ratio_delayLess30Seconds", "ratio_delayLess60Seconds", "ratio_delayLess120Seconds", "ratio_delayLess180Seconds", "ratio_delayLess240Seconds", "ratio_delayLess300Seconds", "ratio_delayMore300Seconds")
    }

    def main(args: Array[String]): Unit = {
        val rootPath = args(0) //GongAnV2
        val date = args(1)

//      System.setProperty("hadoop.home.dir", "D:\\winutil\\")
      val spark = SparkSession.builder()
//          .master("local[*]")
//          .config("spark.sql.warehouse.dir", "c:\\path\\to\\my")
          .appName("dataMonitoring").getOrCreate()

        import spark.implicits._

        var deviceInfoTable = Seq(1, 2, 3).toDF()

        if (args.length == 3) {
          // D:/Program Files/PuTTY/basic_device_info.txt
          deviceInfoTable = spark.read.textFile(args(2)).map(line => {
            val arr = line.split("\t")

            val gbNo = arr(0).substring(1, arr(0).length-1)
            val station_name = arr(14).substring(1, arr(14).length-1)
            (gbNo, station_name)
          }).toDF("gb_code", "station_name")
        } else if (args.length > 3) {
          val url = args(2) //jdbc:postgresql://190.176.32.8:5432/police_traffic
          val deviceInfo = args(3) //basic_device_info
          val user = args(4) //postgres
          val password = args(5) //postgres
          if (args(2).contains("postgresql")) deviceInfoTable = readFromDB(spark, url, deviceInfo, user, password, "org.postgresql.Driver")
          else deviceInfoTable = readFromDB(spark, url, deviceInfo, user, password, "com.mysql.jdbc.Driver")
        }

        val staticDf = deviceInfoTable.filter("station_name = '布吉'").map(row => row.getAs[String]("gb_code")).collect().toSeq
        val bc = spark.sparkContext.broadcast(staticDf)

        var formatDf_ap_raw = Seq(1, 2, 3).toDF()
        var formatDf_sensordoor_face = Seq(1, 2, 3).toDF()
        var formatDf_sensordoor_idcard = Seq(1, 2, 3).toDF()
        var formatDf_ty_imsi = Seq(1, 2, 3).toDF()
        var formatDf_rzx_feature = Seq(1, 2, 3).toDF()
        var formatDf_ajm_idcard = Seq(1, 2, 3).toDF()
        var formatDf_ifaas_face = Seq(1, 2, 3).toDF()
        var formatDf_ifaas_warning = Seq(1, 2, 3).toDF()
        var formatDf_st_status = Seq(1, 2, 3).toDF()
        var formatDf_st_alarm = Seq(1, 2, 3).toDF()

        val deviceTypeList = Seq("ap_raw", "sensordoor_face", "sensordoor_idcard", "ty_imsi", "rzx_feature", "ajm_idcard", "ifaas_face", "ifaas_warning", "st_status", "st_alarm")
//        val deviceTypeList = Seq("rzx_feature", "ifaas_face", "st_alarm")

        for (deviceType <- deviceTypeList) {
          val dataPath = rootPath + "/" + deviceType + "/" + date
          val data = spark.read.parquet(dataPath)
          if (deviceType == "ap_raw") { //ap不需要计算延时
            import spark.implicits._

            formatDf_ap_raw = data.flatMap(row => {
              val dataCollector = new ArrayBuffer[FormatData]()
              val serverReceiveTimestamp = row.getAs[Long]("serverReceiveTimestamp")
              val sdf = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss")
              val serverReceiveTime = sdf.format(new Date(serverReceiveTimestamp * 1000))
              val gbNo = row.getAs[String]("gbNo")
              val MACs = row.getAs[Seq[Row]]("MACs")

              MACs.map(macs => {
                val timestamp = macs.getAs[Long]("timestamp")
                val time = sdf.format(new Date(timestamp * 1000))
                dataCollector.+=(FormatData(deviceType, serverReceiveTimestamp, serverReceiveTime, gbNo, timestamp, time))
              })
              dataCollector
            }).toDF().filter(row => bc.value.contains(row.getAs[String]("gbNo")) && row.getAs[String]("serverReceiveTime").split(" ")(0).split("-").mkString("") == date).distinct()

          } else if (deviceType == "sensordoor_face") {
            import spark.implicits._
            formatDf_sensordoor_face = data.flatMap(row => {
              val dataCollector = new ArrayBuffer[FormatData]()
              val serverReceiveTimestamp = row.getAs[Long]("serverReceiveTimestamp")
              val sdf = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss")
              val serverReceiveTime = sdf.format(new Date(serverReceiveTimestamp * 1000))
              val gbNo = row.getAs[String]("gbNo")
              val time = row.getAs[String]("time")

              val timestamp = try {
                val dt = sdf.parse(time)
                dt.getTime / 1000
              } catch {
                case _: Exception => 0L
              }
              val captureFaceList = row.getAs[Seq[Row]]("captureFaceList")

              captureFaceList.foreach(_ => {
                dataCollector.+=(FormatData(deviceType, serverReceiveTimestamp, serverReceiveTime, gbNo, timestamp, time)) //其他设备扫描到人脸数据
              })
              dataCollector
            }).toDF().filter(row => bc.value.contains(row.getAs[String]("gbNo")) && row.getAs("timestamp") != 0 && row.getAs[String]("serverReceiveTime").split(" ")(0).split("-").mkString("") == date).distinct()

          } else if (deviceType == "sensordoor_idcard") {
            import spark.implicits._
            formatDf_sensordoor_idcard = data.map(row => {

              val serverReceiveTimestamp = row.getAs[Long]("serverReceiveTimestamp")
              val sdf = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss")
              val serverReceiveTime = sdf.format(new Date(serverReceiveTimestamp * 1000))
              val gbNo = row.getAs[String]("gbNo")
              val time = row.getAs[String]("time")

              val timestamp = try {
                val dt = sdf.parse(time)
                dt.getTime / 1000
              } catch {
                case _: Exception => 0L
              }

              FormatData(deviceType, serverReceiveTimestamp, serverReceiveTime, gbNo, timestamp, time)

            }).toDF().filter(row => bc.value.contains(row.getAs[String]("gbNo")) && row.getAs("timestamp") != 0 && row.getAs[String]("serverReceiveTime").split(" ")(0).split("-").mkString("") == date).distinct()

          } else if (deviceType == "ty_imsi") {
            import spark.implicits._
            formatDf_ty_imsi = data.map(row => {

              val serverReceiveTimestamp = row.getAs[Long]("serverReceiveTimestamp")
              val sdf = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss")
              val serverReceiveTime = sdf.format(new Date(serverReceiveTimestamp * 1000))
              val gbNo = row.getAs[String]("gbNo")
              val timestamp = row.getAs[Long]("capTime")
              val time = sdf.format(new Date(timestamp * 1000))

              FormatData(deviceType, serverReceiveTimestamp, serverReceiveTime, gbNo, timestamp, time)
            }).toDF().filter(row => bc.value.contains(row.getAs[String]("gbNo")) && row.getAs[String]("serverReceiveTime").split(" ")(0).split("-").mkString("") == date).distinct()

          } else if (deviceType == "rzx_feature") {
            import spark.implicits._
            formatDf_rzx_feature = data.map(row => {

              val serverReceiveTimestamp = row.getAs[Long]("serverReceiveTimestamp")
              val sdf = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss")
              val serverReceiveTime = sdf.format(new Date(serverReceiveTimestamp * 1000))
              val gbNo = row.getAs[String]("gbNo")
              val timestamp = row.getAs[Long]("START_TIME")
              val time = sdf.format(new Date(timestamp * 1000))

              FormatData(deviceType, serverReceiveTimestamp, serverReceiveTime, gbNo, timestamp, time)
            }).toDF().filter(row => bc.value.contains(row.getAs[String]("gbNo")) && row.getAs[String]("serverReceiveTime").split(" ")(0).split("-").mkString("") == date).distinct()

          } else if (deviceType == "ajm_idcard") {
            import spark.implicits._
            formatDf_ajm_idcard = data.map(row => {

              val serverReceiveTimestamp = row.getAs[Long]("serverReceiveTimestamp")
              val sdf = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss")
              val serverReceiveTime = sdf.format(new Date(serverReceiveTimestamp * 1000))
              val gbNo = row.getAs[String]("gbNo")
              val time = row.getAs[String]("capTime")

              val timestamp = try {
                val dt = sdf.parse(time)
                dt.getTime / 1000
              } catch {
                case _: Exception => 0L
              }

              FormatData(deviceType, serverReceiveTimestamp, serverReceiveTime, gbNo, timestamp, time)

            }).toDF().filter(row => bc.value.contains(row.getAs[String]("gbNo")) && row.getAs("timestamp") != 0 && row.getAs[String]("serverReceiveTime").split(" ")(0).split("-").mkString("") == date).distinct()

          } else if (deviceType == "ifaas_face") {
            import spark.implicits._
            formatDf_ifaas_face = data.map(row => {

              val serverReceiveTimestamp = row.getAs[Long]("serverReceiveTimestamp")
              val sdf = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss")
              val serverReceiveTime = sdf.format(new Date(serverReceiveTimestamp * 1000))
              val gbNo = row.getAs[String]("gbNo")
              val timestamp = row.getAs[Long]("timestamp")
              val time = sdf.format(new Date(timestamp * 1000))
              FormatData(deviceType, serverReceiveTimestamp, serverReceiveTime, gbNo, timestamp, time)

            }).toDF().filter(row => bc.value.contains(row.getAs[String]("gbNo")) && row.getAs("timestamp") != 0 && row.getAs[String]("serverReceiveTime").split(" ")(0).split("-").mkString("") == date).distinct()

          } else if (deviceType == "ifaas_warning") {
            import spark.implicits._
            formatDf_ifaas_warning = data.map(row => {

              val serverReceiveTimestamp = row.getAs[Long]("serverReceiveTimestamp")
              val sdf = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss")
              val serverReceiveTime = sdf.format(new Date(serverReceiveTimestamp * 1000))
              val gbNo = row.getAs[String]("gbNo")
              val timestamp = row.getAs[Long]("timestamp")
              val time = sdf.format(new Date(timestamp * 1000))
              FormatData(deviceType, serverReceiveTimestamp, serverReceiveTime, gbNo, timestamp, time)

            }).toDF().filter(row => bc.value.contains(row.getAs[String]("gbNo")) && row.getAs("timestamp") != 0 && row.getAs[String]("serverReceiveTime").split(" ")(0).split("-").mkString("") == date).distinct()

          } else if (deviceType == "st_status") {
            import spark.implicits._
            formatDf_st_status = data.map(row => {

              val serverReceiveTimestamp = row.getAs[Long]("serverReceiveTimestamp")
              val sdf = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss")
              val serverReceiveTime = sdf.format(new Date(serverReceiveTimestamp * 1000))
              val gbNo = row.getAs[String]("gbNo")
              val time = row.getAs[String]("dateTime")

              val timestamp = try {
                val dt = sdf.parse(time)
                dt.getTime / 1000
              } catch {
                case _: Exception => 0L
              }

              FormatData(deviceType, serverReceiveTimestamp, serverReceiveTime, gbNo, timestamp, time)

            }).toDF().filter(row => bc.value.contains(row.getAs[String]("gbNo")) && row.getAs("timestamp") != 0 && row.getAs[String]("serverReceiveTime").split(" ")(0).split("-").mkString("") == date).distinct()

          } else if (deviceType == "st_alarm") {
            import spark.implicits._
            formatDf_st_alarm = data.map(row => {

              val serverReceiveTimestamp = row.getAs[Long]("serverReceiveTimestamp")
              val sdf = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss")
              val serverReceiveTime = sdf.format(new Date(serverReceiveTimestamp * 1000))
              val gbNo = row.getAs[String]("gbNo")
              val time = row.getAs[String]("dateTime")

              val timestamp = try {
                val dt = sdf.parse(time)
                dt.getTime / 1000
              } catch {
                case _: Exception => 0L
              }

              FormatData(deviceType, serverReceiveTimestamp, serverReceiveTime, gbNo, timestamp, time)

            }).toDF().filter(row => bc.value.contains(row.getAs[String]("gbNo")) && row.getAs("timestamp") != 0 && row.getAs[String]("serverReceiveTime").split(" ")(0).split("-").mkString("") == date).distinct()

          }
        }

            val formatDf = formatDf_ajm_idcard.union(formatDf_ap_raw)
              .union(formatDf_ifaas_warning).union(formatDf_ifaas_face)
              .union(formatDf_sensordoor_face).union(formatDf_sensordoor_idcard)
              .union(formatDf_rzx_feature).union(formatDf_ty_imsi)
              .union(formatDf_st_alarm).union(formatDf_st_status)

//            val formatDf = formatDf_st_alarm.union(formatDf_ifaas_face).union(formatDf_rzx_feature)

            val generalData = general(formatDf)
            val timeSpanData = timeSpan(formatDf)
            val timeDelayData = timeDelay(formatDf)

            val midResult = generalData.join(timeSpanData, "gbNo").join(timeDelayData, "gbNo")
//            formatDf_st_alarm.filter("gbNo='44039605001320064003'").orderBy("time").show()
//            formatDf_ifaas_face.filter("gbNo='44039605001320063035'").orderBy("time").show()
//            formatDf_rzx_feature.filter("gbNo=").show()

            midResult.map(_.mkString(",")).repartition(1).write.mode("overwrite").text("midResult/" + date)

            midResult.groupBy("date", "deviceType").avg().repartition(1).write.mode("overwrite").option("header", "true").csv("monitoringResult/" + date)

    }

}

/**
  * 格式化后的数据格式
  * @param serverReceiveTimestamp 服务器接收时间戳
  * @param serverReceiveTime 服务器接收时间
  * @param gbNo 国标码
  * @param timestamp 设备扫描数据的时间戳
  * @param time 设备扫描数据的扫描时间
  */
case class FormatData(deviceType: String, serverReceiveTimestamp: Long, serverReceiveTime: String, gbNo: String, timestamp: Long, time: String)
