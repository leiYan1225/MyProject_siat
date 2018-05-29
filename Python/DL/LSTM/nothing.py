
import pandas as pd
import os
import tensorflow as tf
import reader

# default_path = os.path.abspath('.')
#
# """Create reference for correpondence between stations and the line they belong to"""
# name_df = pd.read_csv(default_path + "\\dataset\\input\\raw\\station_id_name.csv",
#                           engine='python',
#                           index_col=None,
#                           header=0)
# station_line_dict = {i:name_df['站点名称'][name_df['线路名称'] == (str(i) + '号线')].values.tolist() for i in [1,2,3,4,5,7,9,11]}
#
# print(name_df)
#
#
# # list
# data = [[2000, 'Ohino', 1.5],
#         [2001, 'Ohino', 1.7],
#         [2002, 'Ohino', 3.6],
#         [2001, 'Nevada', 2.4],
#         [2002, 'Nevada', 2.9]]  # type(data) 为 list
#
# # list to series
# ser = Series(data, index = ['one', 'two', 'three', 'four', 'five'])
#
# # list to dataframe
# df = DataFrame(data, index = ['one', 'two', 'three', 'four', 'five'], columns = ['year', 'state', 'pop'])
#
# # list to array
# ndarray = np.array(data)

# DATA_PATH = 'F:\datasets\PTB_data'
# train_data,valid_data,test_data,_= reader.ptb_raw_data(DATA_PATH)
# x,y = reader.ptb_producer(train_data,4,5)
# with tf.Session() as sess:
#     print(sess.run(x))
import numpy as np

x = np.arange(4)
y = np.ones(5)

print(x)
