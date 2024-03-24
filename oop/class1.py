class Student:
    def __init__(self, first_name, last_name,gender):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
    def get_email(self):
        return f"{self.first_name.lower()}.{self.last_name.lower()}@school.edu"
    def get_full_name(self):
        # return "{} {}".format(self.first_name, self.last_name)
        return "{0} {1}".format(self.first_name, self.last_name)




student_one = Student("Nuredin", "Bedru", "Male")
student_two = Student("Female", "Unknown", "Female")

print(student_one.get_full_name())  

class Table:
    def __init__(self, table_number, capacity):
        self.table_number =  table_number
        self.capacity = capacity
        self.is_occupied = False
    def reserve(self):
        if self.is_occupied:
            return f"Table Number {self.table_number} is Occupied"
        else:
            self.is_occupied = True
            return "Table Number {} is Reserved For User".format(self.table_number)
    def release(self):
        if self.is_occupied:
            self.is_occupied = False
            return f"Table Number {self.table_number} is Release !!"
        else:
            return "Table Number {} is Not Reserved Yet !!!".format(self.table_number)
table_1 = Table("12", 32)
table_2 = Table("17", 32)
print(table_1.reserve())

print(table_2.release())
print(table_2.reserve())
print(table_2.release())
print(table_1.is_occupied)