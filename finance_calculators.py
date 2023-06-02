import math

#This program allows a user to access two different financial calculator, an investment calculator and a bond calculator at Orange Bank.
#The investment calculator allows users to calculate the amount of interest they will earn on their investment  while,
#The bond calculator allows users to calculate the amount of money they have to pay back monthly on a home loan.


#Program asks user to input their name and welcome them
name = input("Welcome to Orange Bank! Please enter your first name: ").capitalize()
print(f"\nHello {name}!,""\nWhat kind of finance calculator would you like to use today?")
print("\n1. investment - to calculate the amount of interest you'll earn on your investment")
print("2. bond - to calculate the amount you'll have to pay back on a home loan")

#Ask users to type in their calculator choice
choice = input("\nEnter either 'investment' or 'bond' from the menu above to proceed: ").lower()

#if user selected 'investment', program proceeds to execute below statement
if choice == "investment":
    investment_amount = float(input("\nEnter the amount of money you want to invest(in pounds): "))
    interest_rate = float(input("Enter the interest rate at which you plan to invest: "))
    investment_years  = int(input("Enter the number of years you want to invest for: "))
    interest = input("Choose the interest type you want. Enter 'simple' or 'compound' to proceed: ").lower()

    #Allows user to choose the kind of interest the investment will be calculated with
    if interest == "simple":
        interest_sim = investment_amount * (1 + (interest_rate/100)* investment_years)
        print(f"\nDear {name}!,\nYour investment of £{investment_amount:,.2f} will be worth £{interest_sim:,.2f} at {interest_rate}% after {investment_years} years of {interest} interest.")
    elif interest == "compound":
        interest_com = investment_amount * pow((1 + interest_rate/100), investment_years)
        print(f"\nDear {name}!,\nYour investment of £{investment_amount:,.2f} will be worth £{interest_com:,.2f} at {interest_rate}% after {investment_years} year(s) of {interest} interest.")
    else:
        print("You have entered an invalid interest type! Please enter 'simple' or 'compound' to proceed.")

#if user selected 'bond', then program proceeds to execute below statement
elif choice == 'bond':
    home_present_value = float(input("\nEnter the present value of the house (in pounds): "))
    bond_interest_rate = float(input("Enter the interest rate for bond: "))
    bond_months = int(input("Enter the number of months you plan to take to repay the bond: "))
    monthly_repayment = (((bond_interest_rate/100) / 12) * home_present_value) / (1- (1 + ((bond_interest_rate/100) / 12)) ** (- bond_months))
    print(f"\nDear {name}!,\nThe monthly repayment for your home loan which is currently valued at £{home_present_value:,.2f} is £{monthly_repayment:,.2f} at {bond_interest_rate}% for the next {bond_months}months")

else: 
     print("You have entered an invalid choice of calculator! Please enter 'investment' or 'bond' to proceed.")   
     