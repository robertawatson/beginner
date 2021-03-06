# A very simple net present value (NPV) calculator.
# NPV is found by summing the discounted values of all future cashflows.

# User inputs the number of periods, a cash flow for each period, and the discount rate.

# For the purposes of calculating the discounted value (NPV):
#   Zero and negativbe values are acceptable.
#   The discount rate must be entered as a decimal, e.g. 9% == 0.09

# As Python lists start w/ index 0:
#   "Period 0" is t=0, e.g. the initial cashflow immeadiately at the start of the series.
#   A user that enters "5" for periods will need to enter 6 cashflows.
#   To correct for the indexing issue, periods += 1 has been included.

import pandas as pd

cashflow = []
discountedvalue = []
period = []

df = pd.DataFrame(columns=['Periods', 'Cashflow', 'Present Value'])

def main():
    welcome()
    periods = int(input('Number of Periods: '))
    periods += 1
    for i in range(periods):
        cf = float(input('Cashflow for Period ' + str(i) + ': '))
        cashflow.append(cf)
        period.append(i)
        print("PERIOD ", i, "CASHFLOW ", cf) # TRY AND PRINT THIS AS A LIST RATHER THAN INDIVIDUALLY
    rate = float(input('Discount Rate (as a decimal): '))
    calc(cashflow,rate)

def welcome():
    print('Welcome.')
    print('This is a simple Net Present Value Calculator.')

def calc(p,r):
    df['Period'] = period
    for cf in p:
        n = period.pop(0)
        fv = cf/((1+r)**n)
        discountedvalue.append(fv)
    npv = sum(discountedvalue)
    data()
    print_out(npv)

def data():
    df['Cashflow'] = cashflow
    df['Present Value'] = discountedvalue
    df.to_csv('Cashflow.csv', index=False)

def print_out(n):
    print('____________________')
    print(df)
    print('____________________')
    print('The Net Present Value of your cashflow inputs is: ', n)

if __name__ == "__main__":
    main()
