# This is Comment
print('Hello World')
age = 20
name = 'Tuan Anh'
print(f'My name is {name} and I am {age} years old')

# Data Type
# String
string = 'this is a string'
print('type of string is: ', type(string))

# Boolean
isNumber = True
print(f'type of {isNumber} is ', type(isNumber))

# Number Type
x = 2
y = 4.5
z = 5j
print(f'type of {x} is: ', type(x))
print(f'type of {y} is: ', type(y))
print(f'type of {z} is: ', type(z))

# List
listNumber = [1, 2, 4, 5, 6]
print(f'type of {listNumber} is: ', type(listNumber))
# Tuple
tupleNumber = (1, 2, 3)
print(f'type of {tupleNumber} is: ', type(tupleNumber))
# Range
rangeNumber = range(5)
print(f'type of {rangeNumber} is: ', type(rangeNumber))

# Dictionary
myProfile = {
  name: 'Tuan Anh',
  age: 20
}
print(f'type of {myProfile} is: ', type(myProfile))

# Set
setNumber = { 1, 2, 3 }
print(f'type of {setNumber} is: ', type(setNumber))
fronzenSetNumber = frozenset({ 1, 2, 3 })
print(f'type of {fronzenSetNumber} is: ', type(fronzenSetNumber))