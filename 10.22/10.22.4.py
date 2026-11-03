balance = 1000
interest_rate = 0.05
year = 0
while year < 4:
    balance = balance + (balance * interest_rate)
    print("===============================")
    print("Year: ", year)
    print("Balance: ", balance)
    print("===============================")
    year = year + 1
