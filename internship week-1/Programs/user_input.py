import math

name = input("Enter your name: ")
print(f"Hello {name}!")

fav_animal = input("What is your favorite animal: ")
fav_color = input("What is your favorite color: ")
print(f"You like {fav_color} {fav_animal}s!")

while True:
    x = input("Enter a number to find its square root: ")
    try:
        x = float(x)
        break
    except:
        print("Wrong input, please try again.")

print(f"The square root of {x} is {math.sqrt(x)}")