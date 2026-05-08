cafes = {
    "cafe1": {"drink": "filter coffee", "price": 40},
    "cafe2": {"drink": "tea", "price": 20},
    "cafe3": {"drink": "matcha", "price": 180},
    "cafe4": {"drink": "green tea", "price": 90}
}

print("\n--- Cafe Menu ---")

for cafe, details in cafes.items():
    print(cafe, "->", details)

print("\nTotal Cafes:", len(cafes))

print("\nCafe1 Details:")
print(cafes["cafe1"])

print("\nDrink in Cafe3:")
print(cafes["cafe3"]["drink"])

print("\nAll Cafe Names:")
print(cafes.keys())

print("\nChecking Cafe2:")
if "cafe2" in cafes:
    print("Cafe2 exists")

print("\nAdding Cafe5")

cafes["cafe5"] = {
    "drink": "iced latte",
    "price": 220
}

for cafe, details in cafes.items():
    print(cafe, "->", details)

print("\nRemoving Cafe4")

cafes.pop("cafe4")

for cafe, details in cafes.items():
    print(cafe, "->", details)