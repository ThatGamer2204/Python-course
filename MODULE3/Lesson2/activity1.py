bill_amt=float(input("Enter yout bill amount :"))
tip_perc=float(input("Enter your tip percentage :"))
tip_amt=(tip_perc/100)*bill_amt
def total_calc(bill_amt,tip_amt):
    total_bill=bill_amt+tip_amt
    total=round(total_bill,2)
    return total
print(f"Your initial bill was ${bill_amt}, including your {tip_perc}% tip, your final total is :\n${total_calc(bill_amt,tip_amt)}")