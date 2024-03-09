class CompanyIndicators:
#  revenue - Выручка, num of share - Число акций, share_cost - рыночная цена
#  акции,
#  profit - Чистая
#  прибыль, asset_value - стоимость активов, book_value - балансовая стоимость
    def __init__(self, name_company, cap_comp, revenue, num_of_share,
                 share_cost,
                 profit, dividend, asset_value, book_value):
        self.name_company = name_company
        self.cap_comp = cap_comp
        self.revenue = revenue
        self.num_of_share = num_of_share
        self.share_cost = share_cost
        self.profit = profit
        self.dividend = dividend
        self.asset_value = asset_value
        self.book_value = book_value

    def tax_profit(self):
        return self.profit * 100 / 80

    def earnings_per_share(self):  # ищет EPS
        return (self.tax_profit() - self.dividend) / self.num_of_share

    def p_e(self):
        return self.share_cost / self.earnings_per_share()

    def p_b(self):
        return self.cap_comp / self.book_value

    def roe(self):
        return (self.profit - (self.profit * 0.2)) / self.cap_comp

    def roa(self):
        return self.profit / self.asset_value

    def company_valuation(self):
        return (f'EPS: {round(self.earnings_per_share(), 2)}\nP/E: '
                f'{round(self.p_e())}\nP/B: {round(self.p_b())}')

    def profitability(self):
        return f'ROE: {round(self.roe(), 3)}\nROA: {round(self.roa(), 3)}'


# show_me_indicators = CompanyIndicators(input('Название компании: '),
#                                        int(input('Капитализация компании: ')),
#                                        int(input('Выручка за 2023 год: ')),
#                                        int(input('Кол-во акций компании в '
#                                                  'свободном обращении: ')),
#                                        int(input('Рыночная стоимость акции: ')),
#                                        int(input('Чистая прибыль: '
#                                                  '')),
#                                        input('Дивиденды за последние 5 лет: '),
#                                        int(input('Стоимость активов компании: '
#                                                  '')),
#                                        int(input('Балансовая стоимость: ')))
# print(show_me_indicators.__dict__)
# print(f'EPS компании {show_me_indicators.name_company}'
#       f':{round(show_me_indicators.earnings_per_share(), 2)}\nP/E компании '
#       f'{show_me_indicators.name_company}: {show_me_indicators.p_e()}\nP/B '
#       f'компании {show_me_indicators.name_company}: {show_me_indicators.p_b()}')

# print(f'EPS компании {show_me_indicators.name_company}:'
#       f' {round(show_me_indicators.earnings_per_share(), 2)}')
# print(f'P/E компании {show_me_indicators.name_company}: '
#       f'{show_me_indicators.p_e()}')
# print(f'P/B компании {show_me_indicators.name_company}: '
#       f'{show_me_indicators.p_b()}')
show_me_indicators = CompanyIndicators('Альфа', 5330000, 326500, 73650, 10, 3000,
                                       0.14, 23000,
                                       20000)
print()


def choice_indicators(ci):
    if ci == 1:
        return (f'Оценка компании {show_me_indicators.name_company}: '
                f'\n{show_me_indicators.company_valuation()}')
    elif ci == 2:
        return (f'Рентабельность компании {show_me_indicators.name_company}:'
                f'\n{show_me_indicators.profitability()}')


show_ci = int(input('Показать оценку компании (1) | Показать рентабельность (2) | Оценить '
                    'компанию по показателям (3): '))
print()
print(choice_indicators(show_ci))
# print(show_me_indicators.earnings_per_share())



# Название компании:
# Капитализация компании: 15800
# Выручка за 2023 год: 10000
# Кол-во акций компании в свободном обращении: 580
# Рыночная стоимость акции: 10
# Чистая прибыль: 3000
# Дивиденды за последние 5 лет: 0.02 0.06 0.10 0.03 0.14
# Стоимость активов компании: 23000
# Балансовая стоимость: 20000