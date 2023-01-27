#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def my_input(text):
    while True:
        try:
            tmp_in = int(input(text))
            if tmp_in < 1: raise Exception(None)
            break
        except Exception as e:
            if e.args and not e.args[0]:
                print('Введенное значение должно быть больше нуля.\n')
            else: 
                print('Введенное значение должно быть числом.\n')   
    return tmp_in


tickets = my_input('Введите количество билетов, которое хотите приобрести: ')
      

print ( '\nВы хотите приобрести %d билет%s' % (tickets, 
        '' if str(tickets)[-1] == '1' and tickets != 11 else (
        'a' if str(tickets)[-1] in '234' else 'ов'))+'\n')


price = 0
for t in range(1, tickets+1):
    age = my_input(f'Введите возраст {t}-го посетителя: ')
    
    if 18 <= age <= 25: 
        price += 990
    elif age > 25: 
        price += 1390
    
print ( '\nИтого:\n  количество билетов: %d\n  общая стоимость: %d руб.\n  %s'%(
        tickets, price*0.9 if tickets > 3 else price, 'Скидка 10% !' if price and tickets>3 else '' ))
