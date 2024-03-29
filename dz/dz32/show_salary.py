from class_salary import payroll_system, hourly_employee, salary_employee, fix_employee


salary_em1 = salary_employee.SalaryEmployee(1, 'Валерий Задорожный', 1500)
hourly_employee1 = hourly_employee.HourlyEmployee(2, 'Илья Кромин', 40, 15)
fix_em3 = fix_employee.FixEmployee(3, 'Николай Хорольский', 1000, 250)
payroll_system = payroll_system.PayrollSystem()
payroll_system.calculate([
    salary_em1,
    hourly_employee1,
    fix_em3
])