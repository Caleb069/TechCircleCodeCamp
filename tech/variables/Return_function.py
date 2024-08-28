#def arithemetic_operations(a,b):
#  return a+b,a-b,a*b,a/b

#add,substract,multiply,divide = arithemetic_operations(10,2)
#Eprint(f"Add: {add}, Substract:{substract}, Multiply:{multiply}, Divide:{divide}") 

#Name,age,height,state = "bob", 1000000, 22222222222222, "United states"
#print(Name)
#print(age)
#print(height)
#print(state)

def infinite_arguments(*args):
  sum = 0
  for arg in args:
    sum += arg
  return sum
sum = infinite_arguments(2,3,4,787,9)
print(sum)