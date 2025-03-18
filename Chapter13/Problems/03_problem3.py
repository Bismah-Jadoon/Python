# write a program to filter a list of numbers which are divisible by 5.

def divisible(n):
    if(n%5 == 0):
        return True
    return False

a = [1, 2, 3, 4, 6432, 13445, 12144, 454543, 5, 65, 45, 25]
f = list(filter(divisible, a))
print(f)