import random

friends = ["Mark S.", "Dylan G.", "Helly R.", "Irving B.", "Burt G.", "Ms. Casey", "Harmony Cobel", "Mr. Milchick",
           "Kier Eagan", "Ricken Hale", ]

# Random Name Picker
# Option 1
print(random.choice(friends))

# Option 2 - if you know the number of items in the list you can chose a random number
random_index = random.randint(0, 9)
print(friends[random_index])