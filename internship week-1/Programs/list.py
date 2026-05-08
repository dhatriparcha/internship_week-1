drinks = ['filter coffee','tea','matcha','green tea','iced latte','affagato','gelato']

def show(drinks):
    print("\n----Drinks Menu----")
    for i, item in enumerate(drinks, 1):
        print(f"{i}. {item}")

show(drinks)
print("Length:\n", len(drinks))
print("Type:\n", type(drinks))
print("First item:\n", drinks[0])
print("Second last:\n", drinks[-2])
print("Slice [1:3]:\n", drinks[1:3])
print("First 4:\n", drinks[:4])
print("From index 3:\n", drinks[3:])

if 'tea' in drinks:
    print("Tea is in the list!\n")

drinks[4:5] = ['apple juice\n']  
drinks.insert(3, 'cappuccino\n')
show(drinks)

drinks.append('orange juice\n')
show(drinks)

drinks.pop(2)
show(drinks)