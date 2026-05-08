
f = open("facts.txt", "w")
f.write("1. Hyderabad is capital of telangana.\n")
f.write("2. It is prolly best place to live in India.\n")
f.write("3. It has great travel spots\n")
f.write("4. The Food is great too\n")
f.close()
print("Facts file created!")

f = open("facts.txt", "r")
print(f.read())
f.close()

f = open("facts.txt", "r")
print("First facts:", f.readline())
f.close()


f = open("facts.txt", "r")
lines = f.readlines()
print("Total no.of facts:", len(lines))
f.close()

f = open("facts.txt", "a")
f.write("5. Hyd traffic is insane though\n")
f.close()
print("New fact added!")


f = open("facts.txt", "r")
print(f.read())
f.close()

