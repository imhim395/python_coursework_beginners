inp = input("what do you want: ")
rev = ""
for item in range(len(inp) -1, -1, -1):
    rev += inp[item]

print(rev)

