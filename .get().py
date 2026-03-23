birth_years = {1994: "bill", 1969: "emily", 1982: "elizabeth", 2000: "turner"}
if 1975 in birth_years:
    print(birth_years[1975])
else:
    print("not there")

#checking for the key 1975 in birth years dictionary and if it's not there, then print out a message saying that it's not there
#this takes a while

print(birth_years.get(1975, "not there"))#this is faster, it checks whether 1975 is a key in the dictionary in one line of code and if it isn't then print out a message saying that it's not there