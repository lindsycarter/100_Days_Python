capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Nested list in a Dictionary

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"],
}

# to print only Lille
print(travel_log["France"][1])


nested_list = ["A", "B", ["C", "D"]]
# print only "D" from this nested list
print(nested_list[2][1])

new_travel_log = {
  "France": {
    "cities_visited": ["Paris", "Lille", "Dijon"],
    "total_visits": 12
   },
  "Germany": {
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
    "total_visits": 5
   },
}
# print "Stuttgart" from this nested list and dictionary
print(new_travel_log["Germany"]["cities_visited"][2])