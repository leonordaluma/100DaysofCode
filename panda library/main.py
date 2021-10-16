import pandas

data = pandas.read_csv("weather_data.csv")
# print(data["temp"])
# print(type(data))

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(temp_list)

# total = 0
# length = len(temp_list)
# for _ in temp_list:
#     total += _
# total /= length
# print(round(total))
# print(data["temp"].max())


# print(data["condition"])        
# print(data.condition)

print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(monday.condition)