print("==================\nArea Calculator 📐\n==================")


user_choice = 0

while user_choice != 5:
    user_choice = int(input("1) Triangle\n2) Rectangle\n3) Square\n4) Circle\n5) Quit\n\nWhich Shape: "))
    if user_choice == 1:
        base = float(input("\nBase: "))
        height = float(input("Height: "))
        area = (height * base) / 2
        print(f"The area is: {round(area, 1)}\n-----")
        
    elif user_choice == 2:
        length = float(input("\nLength: "))
        width = float(input("Width: "))
        area = length * width
        print(f"The area is: {round(area, 1)}\n-----")
        
    elif user_choice == 3:
        side = float(input("\nSide: "))
        area = side ** 2
        print(f"The area is: {round(area, 1)}\n-----")
        
    elif user_choice == 4:
        radius = float(input("\nRadius: "))
        area = 3.14 * (radius ** 2)
        print(f"The area is: {round(area, 1)}\n-----")
        
print("Program Quit")

        
        