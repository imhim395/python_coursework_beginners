#they are immutable datatypes
birth_years = {1994: "bill", 1969: "emily", 1982: "elizabeth", 2000: "turner"}
print(birth_years)
people = birth_years
people[1982] = "madeline"
print(birth_years)

#u can use len() to find the length of the key value pairs