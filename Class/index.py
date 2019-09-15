class User:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  
  def showInfo(self):
    print(f'Name: {self.name}, Age: {self.age}')

newUser = User('Tuan Anh', 20)
newUser.showInfo()

# Inheritance
class Student(User):
  def __init__(self, name, age, work):
    User.__init__(self, name, age)
    self.work = work

  def showJob(self):
    print(f'I am a {self.work}')

newStudent = Student('Tuan Anh', 20, 'Primary Student')
newStudent.showInfo()
newStudent.showJob()
