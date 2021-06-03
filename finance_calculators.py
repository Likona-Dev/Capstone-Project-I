import math

# print opening statement to explain the program to the user.
print("""Choose either 'investment' or 'bond' from the menu below to proceed: \n
investment   - to calculate the amount of interest you'll earn on interest
bond         - to calculate the amount you'll have to pay on a home loan""")

# ask user to enter their choice.
finance_type = input("\nEnter either 'investment' or 'bond' to proceed to calculations: ")

# change user input to lower case.
finance_type = finance_type.lower()

# if user enters ‘investment’, ask user to choose the type of interest “simple” or “compound”, then use formula of specified interest type.
# if user enters 'bond', use bond repayment formula and display the answer.
# if user input  is incorrect print out an error message.
if finance_type == "investment":
 principal_amount = float(input("""\nEnter the amount you are depositing:
(Only enter numbers, enter 2500 not R2500)\n"""))
 interest_rate = float(input("""\nEnter the interest rate: E.g. 8 \n"""))
 time = float(input("\nEnter the number of years you plan on investing for: \n"))
 interest = input("""\nChoose “simple” or “compound” interest:
(Enter only 'simple' or 'compound')\n""").lower()
 if interest == "simple":
  amount = principal_amount * (1 + (interest_rate / 100) * time)
  print(f"\nThe amount you'll get is R{amount:.2f}")
 elif interest == "compound":
  amount = principal_amount * math.pow((1 + (interest_rate / 100)), time)
  print(f"\nThe amount you'll get is R{amount:.2f}")
if finance_type == "bond":
    principal_amount = float(input("""\nEnter the present value of the house:
 (Only enter numbers, enter 250000 and not R250000)\n"""))
    interest_rate = float(input("""\nEnter the interest rate: E.g. 8 \n"""))
    time = float(input("\nEnter the number of months you plan to take to repay the bond: E.g. 136 \n"))
    interest_rate = float((interest_rate /100) / 12)
    monthly_pay = (interest_rate * principal_amount) / (1 - (1 + interest_rate) ** (-time))
    print(f"\nYour monthly repayments will be R{monthly_pay:.2f}")

elif (finance_type != "investment") and (finance_type != "bond"):
    print("Error!, Incorrect data entered.")