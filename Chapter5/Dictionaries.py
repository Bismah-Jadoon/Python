dictonary = {
    "Shine": 100,
    "Shimmer": 200,
     "list": [1,2,6]
}
# dictonary = {} # Empty dictionary represented by this

# print(dictonary["list"])
# print(dictonary)
# print(dictonary.items()) #print it in the form of tuples 
# print(dictonary.keys()) 
# print(dictonary.values()) 
# dictonary.update({"Shine":99}) #it will update Shine in the list bcz dictonaries are mutable
# dictonary.update({"Shine":99, "Glimmer":50}) #it will add new entry in the dictonary
# print(dictonary)


print(dictonary.get("Shine")) #it will print value of Shine
print(dictonary["Shine"]) #it will also print value of shine, the only difference between them is if we want to print something that is not in the dictonary then this [] bracket function give type error and the .get() function give None

print(dictonary.get("Dash")) #it will print None
print(dictonary["Dash"]) # it will print TypeError