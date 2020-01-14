class Employee:
   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print ("Всего сотрудников %d" % Employee.empCount)

   def displayEmployee(self):
      print ("Имя : ", self.name,  ", Зарплата: ", self.salary)



emp1 = Employee("AndreyEx", 80000)
emp2 = Employee("Alex", 65000)
emp1.displayEmployee()
emp2.displayEmployee()
print ("Всего сотрудников %d" % Employee.empCount)