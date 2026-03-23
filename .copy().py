birth_years = {1994: "bill", 1969: "emily", 1982: "elizabeth", 2000: "turner"}
print(birth_years)
people = birth_years.copy()
people[1982] = "madeline"
print(birth_years)