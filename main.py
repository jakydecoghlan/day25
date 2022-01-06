import pandas
from numpy import mean

data = pandas.read_csv("weather_data.csv")
# print(data)

# print(data["temp"])
#
# # open ("weather_data.csv")
# data_dict = data.to_dict()
#
# temp_list = data["temp"].to_list()
#
# avg_temp = mean(temp_list)
# print(avg_temp.round(2))
# # print(type(avg_temp))
#
# temp_sum = sum(temp_list)
# # print(temp_sum)
# avg_temp_barrani = temp_sum/len(temp_list)
# # print(type(avg_temp_barrani))
#
# print(round(avg_temp_barrani, 2))
#
#
# print(round(data["temp"].mean(), 2))
#
#
# print(data["temp"].max())
max_temp = data.temp.max()

print(data[data.temp == max_temp])