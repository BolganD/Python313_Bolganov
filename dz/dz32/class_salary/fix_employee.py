from dz.dz32.class_salary.salary_employee import SalaryEmployee


class FixEmployee(SalaryEmployee):
    """Сотрудники с фиксированной оплатой + комиссия"""
    def __init__(self, id_em, name, weekly_salary, comm):
        super().__init__(id_em, name, weekly_salary)
        self.comm = comm

    def calculate_payroll(self):
        return self.weekly_salary + self.comm