class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    def get_salary(self):
        raise NotImplementedError("Subclasses must implement get_salary()")

    def display_details(self):
        print(f"Name: {self.name}\nEmployee ID: {self.employee_id}")
