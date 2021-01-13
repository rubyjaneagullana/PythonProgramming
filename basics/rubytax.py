income=float(input("Enter your  yearly income:Rs. "))
totaltax = 0


if income > 0:
    taxable = min([income, 350000])
    income = income - taxable
    print("nontaxable income= Rs.", taxable)
    print("taxable and remaining income=Rs.", income)
    print("your tax for first Rs. 350,000 is:Rs. ",totaltax)




if income > 0:
    taxable = min([income,200000])
    income = income - taxable
    print("taxable income @ 10%=Rs.", taxable)
    print("remaining income=Rs.", income)
    tax10= taxable*.10
    print("Your tax @ 10% is:Rs. ",tax10)
    totaltax=totaltax+tax10


if income > 0:
    taxable = min([income,200000])
    income = income - taxable
    print("taxable income 20%=Rs.", taxable)
    print("remaining income=Rs.", income)
    tax20 =taxable * .20
    print("Your tax @ 20% is :Rs.",tax20)
    totaltax=totaltax+tax20




if income > 0:
    taxable = income
    print("taxable income 30%=Rs.", taxable)
    print("remaining income=Rs.",taxable)
    tax30 = taxable * .30
    print("your tax @ 30% is :Rs.",tax30)
    totaltax=totaltax+tax30


print("Your total tax is Rs.",totaltax)

















