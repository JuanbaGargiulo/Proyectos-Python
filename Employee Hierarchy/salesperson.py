from employee import Employee
class Salesperson(Employee):
    def __init__(self, name, employee_id, sales_target):
        super().__init__(name, employee_id)
        self.sales_target = sales_target

    def get_salary(self):
        base_salary = 5000  # Example base salary for a salesperson
        commission_rate = 0.05  # Example commission rate
        sales_bonus = self.sales_target * commission_rate
        return base_salary + sales_bonus
