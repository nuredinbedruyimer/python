class Restaurant:
    cuisine_type = "Ethiopian"

    def __init__(self, name , address):
        self.name = name
        self.address = address


res1 = Restaurant("Restaurant Maleda", "Adddis Ababa")
res2 = Restaurant("Restaurant Lucy", "Dessie")
#  Instance Variable
print(res2.name)
print(res1.name)
print(res2.address)
print(res1.address)


#  Class Variable
print(res1.cuisine_type)
print(res2.cuisine_type)

#  to modiefy use clss name and update using that

Restaurant.cuisine_type = "Ethiopian and Ertirian"
print(res1.cuisine_type)
print(res2.cuisine_type)
print(Restaurant.cuisine_type)

class Employee:
    employee_count = 0
    company_name = "Naxa-Company"
    def __init__(self, name, position):
        self.name = name
        self.position = position
        Employee.employee_count += 1
    def get_employee_detail(self):
        return f"Employee {self.name} Working at {self.company_name} as {self.position}"
    def get_employee_count(cls):
        return "Total {} Working right now !!".format(cls.employee_count)
    
empl1 = Employee("Employee One", "Maneger")
empl2 = Employee("Employee Two", "Vice-Maneger")
empl3 = Employee("Employee Three", "Human Resource")
empl4 = Employee("Employee Two", "Consultant")
empl5 = Employee("Employee Two", "Customer Service")

# print(empl1.employee_count)
# print(empl1.company_name)
print(empl1.employee_count)
print(Employee.get_employee_count(empl1))




