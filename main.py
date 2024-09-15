# input statements
salary = float(input())
numDependents = float(input())
stateTax = 0
fedrealTax = 0
dependentDeduction = 0
totalWithholding = 0
# calculate taxes here
stateTax = salary * 0.065
fedrealTax = salary * 0.28
dependentDeduction = (salary * 0.025) * numDependents
totalWithholding = stateTax + fedrealTax + dependentDeduction
takeHomePay = salary - totalWithholding
# output statements
print("State Tax: $" + str(stateTax))
print("Federal Tax: $" + str(fedrealTax))
print("Dependents: $" + str(dependentDeduction))
print("Salary: $" + str(salary))
print("Take Home Pay: $" + str(takeHomePay))
