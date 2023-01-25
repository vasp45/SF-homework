#!/usr/bin/env python3
# -*- coding: utf-8 -*-

per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

while True:
	try:
		money = int(input('Введите сумму вклада: '))
		break
	except ValueError:
		print('Введенное значение должно быть числом.\n')

deposit = [money/100*v for v in per_cent.values()]

print ('\nМаксимальная сумма, которую вы можете заработать: %.2f'%(max(deposit)))

