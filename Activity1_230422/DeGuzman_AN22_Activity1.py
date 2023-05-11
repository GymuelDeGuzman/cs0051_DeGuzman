import os

grade1, grade2, grade3, grade4, grade5 = 0, 0, 0, 0, 0

grade1 = int(input("Input 1st score: "))
grade2 = int(input("Input 2nd score: "))
grade3 = int(input("Input 3rd score: "))
grade4 = int(input("Input 4th score: "))
grade5 = int(input("Input 5th score: "))

grdAvg = float((grade1 + grade2 + grade3 + grade4 + grade5)/5)
print("\nYour average grade is ", grdAvg)