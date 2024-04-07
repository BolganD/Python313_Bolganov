from dz.dz32.class_salary.employee import Employee


class HourlyEmployee(Employee):
    """Сотрудники с почасовой оплатой"""
    def __init__(self, id_em, name, hours_worked, hour_rate):
        super().__init__(id_em, name)
        self.hours_worked = hours_worked
        self.hour_rate = hour_rate

    def calculate_payroll(self):
        return self.hours_worked * self.hour_rate