# the code below is how to write a For loop
# numbers = [1,2,3,4,5]
# for item in numbers:
#   print(item)

# the code below is how to write a while loop
# i=0
# while i<len(numbers):
#   print(numbers[i])
#   i=i+1

# the code below is how to write a function
# def function():
#   print('Run')
# function()

array1 = [1, 2, 3, 5, 6]
array2 = [2, 3, 4, 5, 7]

def mergelists(array1,array2):
  return array1+array2

def removeduplicates(array):
  return list(dict.fromkeys(array))

def sortlist(array):
  array.sort()

mergedlists = mergelists(array1,array2)
cleanedlist =  removeduplicates(mergedlists)
sortlist(cleanedlist)
tidylist = removeduplicates(mergelists(array1, array2))
sortlist(tidylist)
print(tidylist)