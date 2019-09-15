annual_salary=float(input("what is your annul salary:"))
portion_down_percentage=float(input("enter your portion down percentage:"))
total_cost=float(input("enter your total cost:"))
monthly_salary=(annual_salary/12)
partial_save=(portion_down_percentage/100)*monthly_salary
print(partial_save)