import pandas

data = pandas.read_csv("2018_central_park_squirrel_data.csv")

gray = len(data[data["Primary Fur Color"] == "Gray"])
black = len(data[data["Primary Fur Color"] == "Black"])
cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])

# Print Number of Squirrels by Color
# print(f"Gray: {gray}")
# print(f"Black: {black}")
# print(f"Cinnamon: {cinnamon}")

# Create new DataFrame
data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black",],
    "Count": [gray, cinnamon, black,]
}

new_dataFrame = pandas.DataFrame(data_dict)
new_dataFrame.to_csv("squirrel_count.csv")
print(new_dataFrame)