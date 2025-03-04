# CSV Method
# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temps = []
#     for row in data:
#         if row[1] != "temp":
#             temps.append(int(row[1]))
#     print(temps)


# Pandas Method
import pandas

# data = pandas.read_csv("weather_data.csv")
# print(type(data))
# Get Data in Column
# print(data["temp"])

# Data to Dictionary
# data_dictionary = data.to_dict()
# print(data_dictionary)

# Data to List
# temp_list = data["temp"].to_list()
# print(temp_list)

# Find Average Temp
# average_temp = data["temp"].mean()
# print(average_temp)

# Find Max Temp
# max_temp = data["temp"].max()
# print(max_temp)

# Get Data in Column
# Column heading gets turned into an attribute
# print(data.condition)

# Get Data in Rows
# print(data[data.day == "Monday"])

# Print row of the day with max temp.
# print(data[data.temp == data.temp.max()])


# Change to Fahrenheit from Celsius
# def cel_to_fahr(celsius):
#     return (celsius * 9/5) + 32


# monday = data[data.day == "Monday"]
#print(cel_to_fahr(monday.temp))


# Create a DataFrame from Scratch
# with this data
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

# create the frame
new_dataFrame = pandas.DataFrame(data_dict)
print(new_dataFrame)
# creates new csv file
new_dataFrame.to_csv("new_dataFrame.csv")