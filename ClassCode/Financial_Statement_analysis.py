##TWO LISTS
##MONTHLY REVENUE AND MONTHLY EXPENSES
import numpy as np

revenueList = [14574.49, 7606.46, 8611.41,9175.41, 8058.65, 8105.44, 11496.28,9766.09,10305.32,14379.96,10713.97,15432.89]
expensesList = [12051.82, 5695.07, 12319.20, 12089.72, 8658.57, 840.20, 3285.73, 5821.12, 6976.93, 16618.61, 10054.37, 3803.45]

#print(len(revenueList))
#print(len(expensesList))


##PROFIT EACH MONTH
##while(i < len(revenueList) and i < len(expensesList)):
##    print(revenueList[i], "-->", expensesList[i])
##    i += 1
profitList = []
profitAfterTaxList = []
profit_each_mon = 0.0
profit_after_tax = 0.0
profit_margin_each_month = 0.0
mean_profit_after_tax = 0.0

i = 0
print('PROFIT EACH MONTH ', ' ', 'PROFIT AFTER TAX', ' ', 'PROFIT MARGIN' )
for rv in revenueList:
##    print(rv, "-->", expensesList[i])
    profit_each_month = rv - expensesList[i]
    profit_after_tax = rv -(expensesList[i] + (rv*.3))
    profit_margin_each_month = profit_after_tax/rv
    print(profit_each_month,
          ' ', profit_after_tax, ' ', profit_margin_each_month)
    profitList.append(profit_each_month)
    profitAfterTaxList.append(profit_after_tax)
    i += 1    

profitAfterTaxArry = np.array(profitAfterTaxList)
mean_profit_after_tax = profitAfterTaxArry.mean()

print('The mean profit after tax ',mean_profit_after_tax)

for pat in profitAfterTaxList:
    print('Profit after tax ',pat > mean_profit_after_tax)


for goodMonth in range(len(profitAfterTaxList)):
    if(profitAfterTaxList[goodMonth] == max(profitAfterTaxList)):
        print(goodMonth+1)

##for p in profitList:
##    print(p)
##
##for p in profitAfterTaxList:
##    print(p)
