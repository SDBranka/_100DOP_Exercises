import pandas

# create csv named squirrel_count.csv
# that shows the count of each fur color

# read in the squirrel_data.csv and store 
#   it in a variable called squirrel_data
squirrel_data = pandas.read_csv("squirrel_data.csv")

# get the fur colors and the count of each
squirrel_colors = squirrel_data["Primary Fur Color"].value_counts()
# print(squirrel_colors)

# convert the format to a dictionary
squirrel_colors_dict = squirrel_colors.to_dict()
# print(squirrel_colors_dict)

# reformat the dictionary
data_dict = {
    "color": [color for color in squirrel_colors_dict.keys()],
    "count": [count for count in squirrel_colors_dict.values()]
}
# print(data_dict)

# create a dataframe from the data_dict dictionary
data = pandas.DataFrame(data_dict)
# write the dataframe to a csv file named squirrel_count.csv
data.to_csv("squirrel_count.csv")