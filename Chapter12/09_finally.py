def main():
   try:
    num = int(input("Enter a number : "))
    print(num)
    return  #if function return it means that no function after return will execute
   
   except Exception as e:
    print(e)
    return 
   
   finally:
    print("I am inside finally") #this will always work but the use case of this finally is that if we are in function and return something it will still 

main()