import pandas

# create csv named squirrel_count.csv
# that shows the count of each fur color

# Primary_Fur_Color

squirrel_data = pandas.read_csv("squirrel_data.csv")

# squirrel_colors = squirrel_data["Primary Fur Color"].value_counts()
# print(squirrel_colors)
# squirrel_colors_dict = squirrel_colors.to_dict()
# print(squirrel_colors_dict)

data_dict = {}
squirrel_colors = squirrel_data["Primary Fur Color"]
print(set(squirrel_colors))
for color in set(squirrel_colors[1:]):
    # print(color, squirrel_colors.value_counts()[color])
    color_count = squirrel_colors.value_counts()[color]
    print(color_count)



# data = pandas.DataFrame(squirrel_colors)
# data.to_csv("squirrel_count.csv")