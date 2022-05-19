import pandas


data = pandas.read_csv("squirrel_data.csv")

# # returns the series of the data
# print(f"1: {data['Primary Fur Color']}")
# # returns a series of data with the fur 
# #   color evaluated as a boolean
# print(f"2: {data['Primary Fur Color'] == 'Gray'}")
# # print data where the fur color is gray
# #  --when the fur color is Gray it is included in the set
# print(f"3: {data[data['Primary Fur Color'] == 'Gray']}")

# count the number of times the fur color is Gray
grey_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
# print(f"grey_squirrels: {grey_squirrels}")
# count the number of times the fur color is Cinnamon
cin_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
# print(f"cin_squirrels: {cin_squirrels}")
# count the number of times the fur color is Black
black_squirrels = len(data[data["Primary Fur Color"] == "Black"])
# print(f"black_squirrels: {black_squirrels}")

data_dict ={
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels, cin_squirrels, black_squirrels]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")