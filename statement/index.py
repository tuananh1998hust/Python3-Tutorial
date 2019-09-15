# If else statement
def checkAge(age):
  if (age <= 0):
    print('Error')
  elif (0 < age < 5):
    print('Baby')
  elif (6 < age < 18):
    print('Student')
  else:
    print('Others')

checkAge(-1)
checkAge(2)
checkAge(10)
checkAge(20)

# While Loops
i = 1
while(i < 5):
  print(f'i = {i}')
  i += 1

# For Loops
listNumber = [1, 2, 3, 4, 5]
for x in listNumber:
  print(x)