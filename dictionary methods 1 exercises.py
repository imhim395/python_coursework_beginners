bandz = {"Queen": "Bohemian Rhapsody",
         "Bee Gees": "Stayin' Alive",
         "U2": "One",
         "Michael Jackson": "Billie Jean",
         "The Beatles": "Hey Jude",
         "Bob Dylan": "Like A Rolling Stone"}
print(len(bandz))

for k in bandz.keys():
    print(k)

print(bandz.values())

for k in bandz.items():
    print(k)

print(bandz.get("Promise of the Real", "not there"))
