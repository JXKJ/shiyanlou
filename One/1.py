import sys

threshold= 3500
insurances = 0
monyForTaxes = 0
taxes=0

for wages in sys.argv[1:]:
	try:
		wages = int(wages)
		print('工资金额为:',wages)
	except ValueError:
		print("请输入正确的工资金额:",ValueError)
	#计算应纳税所得额
	#应纳税所得额 = 工资金额 － 各项社会保险费 - 起征点(3500元)		
	if wages<3500:
		print('你太穷了,无须缴纳个税。')
	else:
		monyForTaxes = wages-insurances-threshold
		print('应纳税所得额:',monyForTaxes)
	#根据条件计算应纳税额
	#应纳税额 = 应纳税所得额 × 税率 － 速算扣除数
	if monyForTaxes<1500:
		taxes = monyForTaxes*0.03-0
	elif monyForTaxes<4500:
		taxes = monyForTaxes*0.1-105	
	elif monyForTaxes<9000:
		taxes = monyForTaxes*0.2-555
	elif monyForTaxes<35000:
		taxes = monyForTaxes*0.25-1005	
	elif monyForTaxes<55000:
		taxes = monyForTaxes*0.3-2755	
	elif monyForTaxes<80000:
		taxes = monyForTaxes*0.35-5505	
	else:
		taxes = monyForTaxes*0.45-13505
	taxes = format(taxes,'.2f')
	print('应纳税额:',taxes)
	print('========================')