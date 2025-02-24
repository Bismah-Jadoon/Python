# Write a program to accept marks of 6 students and then display them in a sorted manner

marks = []

student1 = int(input("Enter marks : "))
marks.append(student1)
student2 = int(input("Enter marks : "))
marks.append(student2)
student3 = int(input("Enter marks : "))
marks.append(student3)
student4 = int(input("Enter marks : "))
marks.append(student4)
student5 = int(input("Enter marks : "))
marks.append(student5) 
student6 = int(input("Enter marks : "))
marks.append(student6) 

marks.sort()

print(marks)