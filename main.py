import pandas
from numpy import mean
#
# data = pandas.read_csv("weather_data.csv")
# # print(data)
#
# # print(data["temp"])
# #
# # # open ("weather_data.csv")
# # data_dict = data.to_dict()
# #
# # temp_list = data["temp"].to_list()
# #
# # avg_temp = mean(temp_list)
# # print(avg_temp.round(2))
# # # print(type(avg_temp))
# #
# # temp_sum = sum(temp_list)
# # # print(temp_sum)
# # avg_temp_barrani = temp_sum/len(temp_list)
# # # print(type(avg_temp_barrani))
# #
# # print(round(avg_temp_barrani, 2))
# #
# #
# # print(round(data["temp"].mean(), 2))
# #
# #
# # print(data["temp"].max())
# max_temp = data.temp.max()
#
# monday = data[data.day == "Monday"]
# monday_temp_farenheit = ((monday.temp) * 9/5) + 32
# print(monday_temp_farenheit)
#
# # create dataframe
#
# data_dict = {
#     "personas": ["juancito", "pablito", "josecito"],
#     "edades": [12, 11, 9]
#
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("nuevo_dataframe")

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")


fur_color_list = data["Primary Fur Color"].to_list()
fur_gray = sum(data["Primary Fur Color"] == "Gray")
fur_black = sum(data["Primary Fur Color"] == "Black")
fur_cinnamon = sum(data["Primary Fur Color"] == "Cinnamon")



squirrel_count_dict = {
    "Fur Color": ["gray", "cinnamon", "black"],
    "Count": [fur_gray, fur_cinnamon, fur_black]

}
squirrel_count = pandas.DataFrame(squirrel_count_dict)
squirrel_count.to_csv("squirrel_count")