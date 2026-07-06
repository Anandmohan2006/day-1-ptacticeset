f = open("poem.txt", "r")

poem = f.read()

if "twinkle" in poem:
    print("poem is correct")
else:
    print("poem is incorrect")

print(poem)

f.close()