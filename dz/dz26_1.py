import re


class Account:
    rate_usd = 0.013
    rate_eur = 0.011
    su_r = 'RUB'
    su_u = 'USD'
    su_e = "EUR"

    def __init__(self, surname, num, percent, value=0):
        self.surname = surname
        self.num = num
        self.percent = percent
        self.value = value
        print(f'Счет #{self.num} принадлежащий клиенту {self.surname} был '
              f'открыт.')
        print('*' * 50)

    @property
    def surname(self):
        return self.__surname

    @property
    def num(self):
        return self.__num

    @property
    def percent(self):
        return self.__percent
    @property
    def value(self):
        return self.__value

    @surname.setter
    def surname(self, surname):
        self.v_sn(surname)
        self.__surname = surname

    @num.setter
    def num(self, num):
        self.v_num(num)
        self.__num = num

    @percent.setter
    def percent(self, percent):
        self.v_per(percent)
        self.__percent = percent

    @value.setter
    def value(self, value):
        self.v_val(value)
        self.__value = value

    def __del__(self):
        print('*' * 50)
        print(f'Счет №{self.num} принадлежащий клиенту {self.surname} был '
              f'закрыт.')

    @classmethod
    def set_usd_rate(cls, rate):
        cls.rate_usd = rate

    @classmethod
    def set_eur_rate(cls, rate):
        cls.rate_eur = rate

    @staticmethod
    def convert(value, rate):
        return value * rate

    @staticmethod
    def v_sn(surname):
        if not isinstance(surname, str):
            raise TypeError('Фамилия клиента должна быть строкой')
        f = surname.split()
        if len(f) != 1:
            raise TypeError("Неверный формат фамилии клиента")
        let = "".join(re.findall("[a-zа-яё-]", surname, re.IGNORECASE))
        for li in f:
            if len(li.strip(let)) != 0:
                raise TypeError(
                    "В фамилии клиента можно использовать только буквы и дефис")

    @staticmethod
    def v_num(num):
        if not isinstance(num, str):
            raise TypeError('Номер счета необходимо вводить строкой')
        if len(num) > 6:
            raise TypeError('Неверный формат номера счета')

    @staticmethod
    def v_per(percent):
        if not isinstance(percent, (int, float)):
            raise TypeError('Проценты должны вводиться вещественным числом')
        if percent < 0 or percent > 1:
            raise TypeError('Проценты должны вводиться от 0 до 1')

    @staticmethod
    def v_val(value):
        if not isinstance(value, (int, float)):
            raise TypeError('Значение должно задаваться числом')

    def convert_to_usd(self):
        usd_val = Account.convert(self.value, Account.rate_usd)
        print(f'Состояние счета в долларах: {usd_val} {Account.su_u}')

    def convert_to_eur(self):
        eur_val = Account.convert(self.value, Account.rate_eur)
        print(f'Состояние счета в евро: {eur_val} {Account.su_e}')

    def print_balance(self):
        print(f'Текущий баланс: {self.value} {Account.su_r}')

    def edit_owner(self, surname):
        self.__surname = surname

    def add_percent(self):
        self.value += self.value * self.percent
        print('Проценты были успешно начислены')
        self.print_balance()

    def withdraw_money(self, val):
        if val > self.value:
            print(f"К сожалению у вас нет {val} {Account.su_r}")
        else:
            self.value -= val
            print(f'{val} {Account.su_r} было успешно снято.')
        self.print_balance()

    def add_money(self, val):
        self.value += val
        print(f'{val} {Account.su_r} было успешно добавлено.')
        self.print_balance()

    def print_info(self):
        print('Информация о счете:')
        print('-' * 20)
        print(f'#{self.num}')
        print(f'Владелец: {self.__surname}')
        self.print_balance()
        print(f'Проценты: {self.percent:.0%}')
        print('-' * 20)


acc = Account('Долгих', '12345', 0.03, 1000)
acc.print_info()
acc.convert_to_usd()
acc.convert_to_eur()
Account.set_usd_rate(2)
acc.convert_to_usd()
Account.set_eur_rate(1)
acc.convert_to_eur()
acc.edit_owner('Дюма')
acc.print_info()
acc.add_percent()
print()
acc.withdraw_money(100)
print()
acc.withdraw_money(3000)
print()
acc.withdraw_money(500)
print()
acc.add_money(4470)
print()
acc.withdraw_money(3000)



