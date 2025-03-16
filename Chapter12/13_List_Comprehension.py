list = [1,2,3,4,5]

# squareList = []
# for item in list:
#     squareList.append(item*item)

# it can be done with listComprehension
squareList = [i*i for i in list]
print(squareList)