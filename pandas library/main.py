import pandas

data = pandas.read_csv("census.csv")
black = data[data["Primary Fur Color"]  == "Black"]
grey = data[data["Primary Fur Color"]  == "Gray"]
red = data[data["Primary Fur Color"]  == "Cinnamon"]

data_dict = {
    "Fur Color": ["grey", "red", "black"],
    "Count": [len(grey), len(red), len(black)]
}

squirrel_data = pandas.DataFrame(data_dict)
squirrel_data.to_csv("squirrel_count.csv")