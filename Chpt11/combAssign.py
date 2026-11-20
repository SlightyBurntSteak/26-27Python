# --------------------------
# Section 11.4 Practice: Combining Assignment and Arithmetic
# Each Shortcut operator updates a variable using its current value
# --------------------------

# --- Basic idea ---------
total = 10
cans = 4
total += cans
print("total += cans ----->", total)  # 14

total *= 2
print("total *= 2 -------->" , total) #28

# --- Count by one -----------
count = 0
count += 1
count += 1
count += 1
count += 1
count += 1
count += 1

print("count = ", count)

# --- Realistic use: a running total (shopping cart) ----------

cartTotal = 0.0
cartTotal += 3.49 # notebook
cartTotal += 12.99 # USB drive
cartTotal += 1.25 # pencils

print("\n Your cart total today is: $", str(round(cartTotal, 2)))
