#!/usr/bin/env python3
# -*- coding: utf-8 -*-

per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

while True:
    try:
        money = int(input('Введите сумму вклада: '))
        break
    except ValueError:
        print('Введенное значение должно быть числом.\n')

deposit = {key:money/100*v for key, v in per_cent.items()}

print ( '\nМаксимальная сумма, которую вы можете заработать: '+
        '{0[1]:.2f}, банк: {0[0]:s}'.format(
        (max(deposit.items(), key=lambda v: v[1]))))

