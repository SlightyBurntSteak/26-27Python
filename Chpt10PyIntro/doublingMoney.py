# =====================================
# Script Name: doublingMoney.py
# Lesson: Algorithms Design (Section 10.9)
#
#
# Problem: 
#   You put $10,000 into an account that earns 5% interest per year. How many   years until the balance doubles?
#
#
# Pseudocode (My algorithm):
#   Set year to 0, balance to 10000
#   While balance is less than 20000
#       Add 1 to the year.
#       Set the interest to balance x 0.05.
#       Add the interest to the balance.
#   Report the year as the answer.
# ======================================

# Set year to 0, Balance to 10000
year = 0
balance = 10000

# While balance is less than 20000
while balance < 20000: # The loop will continue until the balance is at least 20000
    # Add 1 to the year.
    year += 1
    # Set the interest to balance x 0.05.
    interest = balance * 0.05
    # Add the interest to the balance.
    balance += interest

# Report the year as the answer.
print("-====================================-")
print("Years to double:", year)
print("Final balance:", f"${balance:.2f}")
print("-====================================-")

