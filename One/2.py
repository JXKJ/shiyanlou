import sys

threshold= 3500
insurances = 0
monyForTaxes = 0
taxes=0
for wages in sys.argv[1:]:
	try:
		wages = int(wages)
	except ValueError:
		print('Parameter Error')
	if wages<3500:
		print('You\'re too poor to pay a tax.')
	else:
		monyForTaxes = wages-insurances-threshold

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
	taxes = format(taxes,".2f")
	print(taxes)
	