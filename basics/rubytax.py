income=float(input("enter your  yearly salary: "))
if income > 0:
    taxable = min([income, 350000])
    income = income - taxable
    print("taxable income=", taxable)
    print("remaining income=", income)
    totaltax=0



if income > 0:
    taxable = min([income,200000])
    income = income - taxable
    print("taxable income=", taxable)
    print("remaining income=", income)
    totaltax= taxable*.10
    print("total tax is :",totaltax)

if income > 0:
    taxable = min([income,200000])
    income = income - taxable
    print("taxable income=", taxable)
    print("remaining income=", income)
    totaltax =totaltax + (taxable * .20)
    print("total tax is :",totaltax)

if income > 200000:
    taxable = income
    print("taxable income=", taxable)
    tax3 = taxable * .30
    print("tax at 30% is :",tax3)
    totaltax = totaltax+tax3
    print("total tax: ",totaltax)
















