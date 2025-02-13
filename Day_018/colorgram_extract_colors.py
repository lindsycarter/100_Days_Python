import colorgram

# create empty list
rgb_colors = []
# extract colors
colors = colorgram.extract('image.jpg', 30)

# for each of the colors...
for color in colors:
    red = color.rgb.r
    green = color.rgb.g
    blue = color.rgb.b
    # create rgb tuple
    new_color = (red, green, blue)
    # ...add the tuple as variable to the rgb_list
    rgb_colors.append(new_color)

print(rgb_colors)

# you get this list:
# [(208, 158, 96), (234, 213, 101), (41, 104, 144), (149, 78, 57), (130, 168, 194), (202, 137, 162), (148, 65, 83),
# (24, 40, 55), (204, 90, 68), (169, 159, 55), (139, 180, 152), (193, 89, 121), (59, 117, 93), (26, 44, 36),
# (223, 171, 187), (63, 46, 34), (91, 154, 104), (44, 161, 182), (237, 212, 7), (226, 175, 167), (13, 96, 75),
# (41, 59, 99), (179, 189, 213), (99, 125, 168), (65, 33, 43), (104, 43, 59)]