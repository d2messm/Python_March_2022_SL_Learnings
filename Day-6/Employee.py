class Employee:
    def readData(self):
        self.id=int(input("Enter employee id:"))
        self.name=input("Enter employee name:")
        self.salary=int(input("Employee employee salary:"))
    def printData(self):
        print("Id=",self.id)
        print("Name=",self.name)
        print("Salary=",self.salary)
        print("Company=","Microsoft")
    def printCompany():
        print("Company=","Microsoft")
e=Employee()
e.readData()
e.printData()

del e

e.printData()

        


