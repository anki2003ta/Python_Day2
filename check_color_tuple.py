def get_colors_from_user():
    colors = []
    for i in range(3):
        print(f"Enter colors for tuple {i+1}:")
        color1 = input("Color 1: ")
        color2 = input("Color 2: ")
        color3 = input("Color 3: ")
        colors.append((color1, color2, color3)) 	
    return tuple(colors)#((color1, color2, color3),(color1, color2, color3),(color1, color2, color3))
#[(color1, color2, color3)]->for i=0 
#[(color1, color2, color3),(color1, color2, color3)]->for i=1
#[(color1, color2, color3),(color1, color2, color3),(color1, color2, color3)]->for i=2
def check_color_in_tuple(colors, target_color):
    for color_tuple in colors:
        if target_color in color_tuple:
            return True
    return False

def main():
    colors = get_colors_from_user()
    print("Tuple of tuples:", colors)
    target_color = input("Enter a color to search: ")
    if(check_color_in_tuple(colors, target_color)):
        print(f"{target_color} exists in the tuple.")
    else:
        print(f"{target_color} does not exist in the tuple.")
if __name__ == "__main__":
    main()


