deposit =float(input("enter your investment amount:     "))

for x in range(1, 30):
  return_on_investment= deposit *0.10
  new_amount = return_on_investment+ deposit
  deposit = new_amount
  print(f"your return_on_investment is N{return_on_investment:},investment is now{new_amount}")
