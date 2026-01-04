#this is an example with the scenario being a rising college freshman applying for a student loan

gpa=float(input("What is the applicants GPA?"))
institution_app=input("Is the student going to an approved institution? ")
if gpa >=3.7:
    if institution_app=="yes":
        print("The applicant qualifies for the student loan")
    else:
        print("The applicant doesn't qualify for the student loan")
else:
    print("The applicant doesn't have high enough grades for the student loan")
