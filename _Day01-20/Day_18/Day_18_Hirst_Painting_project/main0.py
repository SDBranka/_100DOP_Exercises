###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import colorgram

rgb_colors = []
colors = colorgram.extract('image.jpg', 6)

for color in colors:
    rgb_colors.append(color.rgb)

print(rgb_colors)

rbg_as_tuples = []
# to get as tuple
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rbg_as_tuples.append((r, g, b))

print(rbg_as_tuples)