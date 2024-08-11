# Take limitation of tuple from user
limit = int(input("Enter the number of months: "))

# Take input for tuple from user
monthly_incomes = []
for i in range(limit):
    month = input(f"Enter month {i+1}: ")
    income = int(input(f"Enter income for {month}: "))
    monthly_incomes.append((month, income))

months, incomes = zip(*monthly_incomes)

total_income = sum(incomes)

print(f"Total income : {total_income}\n")

quarters = [
    monthly_incomes[:3],
    monthly_incomes[3:6], 
    monthly_incomes[6:9],   
    monthly_incomes[9:]     
]

for quarter in quarters:
    quarter_total = sum(income for _, income in quarter)
    for month, income in quarter:
        print(f"{month}: {income}")
    print("--------------------")
    print(f"Quarter: {quarter_total}\n")