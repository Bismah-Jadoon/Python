# write a program to find out whether a student is pass or fail, if it requires total 40% and atleast 33% in each subject to pass.Assume 3 subjects and take marks as an input from the user

marks1 = int(input("Enter marks of subject 1: "))
marks2 = int(input("Enter marks of subject 2: "))
marks3 = int(input("Enter marks of subject 3: "))

total_percentage = (100 * (marks1 + marks2 + marks3)/300)


if(total_percentage > 40 and marks1 >= 33 and marks2 >= 33 and marks3 >= 33):
    print("You are pass", total_percentage)

else:
    print("You are fail", total_percentage)