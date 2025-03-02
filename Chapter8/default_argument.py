def greet(name, ending = "Thank You"):
    print(f"Good Day! {name}")
    print(ending)

greet("Shine", "Thanks") #if a value is given to a parameter than it will print that value in this case it will print Thanks 
greet("Shimmer") #if the value is not given to a parameter it will print the default value in this case it will print Thank You