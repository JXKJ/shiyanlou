#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

threshold= 3500
#各项保险费率之和，实验使用，默认写死（实际中需要计算各项保险费率）
insurances = 0.165
monyForTaxes = 0
taxes=0
shuilv=0.0
jishu=0
for wages in sys.argv[1:]:
	wageInfo =wages.split(':')
	JobNum = wageInfo[0]
	try:
		wages = int(wageInfo[1])
	except ValueError:
		print('Parameter Error')
	if wages<3500:
		print('You\'re too poor to pay a tax.')
	else:
		monyForTaxes = wages-(wages*insurances)-threshold
	
	if monyForTaxes<0:
		monyForTaxes=0
	elif 0<monyForTaxes<1500:
		shuilv = 0.03
	elif monyForTaxes<4500:
		shuilv = 0.1
		jishu=105
	elif monyForTaxes<9000:
		shuilv = 0.2
		jishu=555
	elif monyForTaxes<35000:
		shuilv = 0.25
		jishu=1005
	elif monyForTaxes<55000:
		shuilv = 0.3
		jishu=2755
	elif monyForTaxes<80000:
		shuilv = 0.35
		jishu=5505
	else:
		shuilv = 0.45
		jishu=13505
	#计算应交个人所得税
	taxes = monyForTaxes*shuilv-jishu
	wages = format(wages-taxes-(wages*insurances),".2f")
	#格式化输出个人税后工资
	print("%s:%s"%(JobNum,wages))
	