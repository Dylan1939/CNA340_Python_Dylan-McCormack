red = int(input())
green = int(input())
blue = int(input())

num1 = (red, green, blue)
a = min(num1) 
gray_colors_red = (red - a) 
gray_color_green = (green - a)
gray_color_blue = (blue - a)
print(gray_colors_red, gray_color_green, gray_color_blue)
