
from manager import Manager
from engineer import Engineer
from salesperson import Salesperson


manager = Manager("John Doe", 1001, "Sales")
engineer = Engineer("Jane Smith", 1002, "Python")
salesperson = Salesperson("Bob Johnson", 1003, 100000)

manager.display_details()
print("Salary:", manager.get_salary())

print()

engineer.display_details()
print("Salary:", engineer.get_salary())

print()

salesperson.display_details()
print("Salary:", salesperson.get_salary())
