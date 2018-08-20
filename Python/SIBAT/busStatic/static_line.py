import pandas as pd

data = pd.read_csv('F:\BusOD\lineAndStation_zone',
                   names=["line_id","direction","station_id","station_name","station_index","lat","lon","zone"],
                   index_col="line_id")
print(data)