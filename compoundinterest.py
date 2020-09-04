#Prompts user to input dollar amount as an integer
dollars = int(input("Dollars I want to invest: "))
#Prompts user to input number of years as an integer
years = int(input("Years I want to invest: "))
#Prints and computes expected return given a 7 percent growth rate
print(dollars * (pow(1.07, years)))