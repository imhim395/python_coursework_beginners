asciibetical = ["Andy", "kiwi", "apple", "Karen", "Brian", "banana"]
asciibetical.sort()
print(asciibetical)



asciibetical = ["Andy", "kiwi", "apple", "Karen", "Brian", "banana"]
asciibetical.sort(key=str.lower)#sorts in alpha order
print(asciibetical)