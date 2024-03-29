from class_salary import employee


class SalaryEmployee(employee.Employee):
    """Административные работники с фиксированной зп"""

    def __init__(self, id_em, name, weekly_salary):
        super().__init__(id_em, name)
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary
