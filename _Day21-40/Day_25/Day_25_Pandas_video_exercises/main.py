import pandas

# read the csv using pandas
weather_data = pandas.read_csv("weather_data.csv")

# # print the weather_data as a dataframe object
# print(weather_data)
# print(type(weather_data))    #<class 'pandas.core.frame.DataFrame'>

# # print the temp column from 
# #  weather_data as a series object
# print(weather_data["temp"])
# print(type(weather_data["temp"]))    #<class 'pandas.core.series.Series'>

# create dictionary of the weather_data
weather_dict = weather_data.to_dict()
# print(weather_dict)

temp_list = weather_data["temp"].to_list()
# print(temp_list)
# print(type(temp_list))    #<class 'list'>
# print(len(temp_list))

# # print the average of the temp_list
# avg_temp = sum(temp_list) / len(temp_list)
# print(avg_temp)

# get the average of the temp_list using pandas
avg_temp = weather_data["temp"].mean()
# print(avg_temp)

# get the max temp using pandas
max_temp = weather_data["temp"].max()
# print(max_temp)

# a way to access a series
#     will produce same result as
#     weather_data["temp"] 
# print(weather_data.temp)

# get data from the rows in weather_data
# where the day is a Monday
monday_row = weather_data[weather_data["day"] == "Monday"]
# print(monday_row)

# get the row from weather_data where the temp
# is the maximum
max_temp_row = weather_data[weather_data["temp"] == max_temp]
# print(max_temp_row)

# using data from [an] accessed row(s)
monday = weather_data[weather_data.day == "Monday"]
# print(monday.condition)

# convert temp in celcius to fahrenheit
monday_c_temp = monday.temp[0]
# print(monday_c_temp)
monday_f_temp = (monday_c_temp * 9/5) + 32
print(monday_f_temp)

# create a dataframe from scratch
data_dict = {
    "students": ["Rolf", "Charlie", "Anna", "Jen"],
    "scores": [76, 82, 91, 87]
}

data = pandas.DataFrame(data_dict)
print(data)
# write the data to a csv file
data.to_csv("scores.csv")