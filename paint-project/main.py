import colorgram

hurst_colors = colorgram.extract('image.jpg', 12)

def get_rgb(cg_colors):
    colors = []

    for color in cg_colors:
        color_tuple = (color.rgb.r, color.rgb.g, color.rgb.b)
        colors.append(color_tuple)

    # need to check tuples within list
    # check for white colors within
    # remove white values
    return colors
    
print(get_rgb(hurst_colors))
