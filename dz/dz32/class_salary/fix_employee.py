from class_salary import salary_employee


class FixEmployee(salary_employee.SalaryEmployee):
    """Сотрудники с фиксированной оплатой + комиссия"""
    def __init__(self, id_em, name, weekly_salary, comm):
        super().__init__(id_em, name, weekly_salary)
        self.comm = comm

    def calculate_payroll(self):
        return self.weekly_salary + self.comm