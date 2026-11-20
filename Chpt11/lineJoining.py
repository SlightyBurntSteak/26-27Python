# --------------------------
# Section 11.5 Practice: Line Joining
# Splitting long statements across multiple lines. 
# --------------------------

from math import sqrt

a = 1
b = -3 
c = 2

# ---- Implicit joining: break the line INSIDE parentheses ---------
# This is the preferred style

x1 = ((-b + sqrt(b ** 2 - 4 * a * c)) 
    / (2 * a))

print("x1 (parentheses) = ", x1)

# ---- Explicit joining: end the line with a backslash ---------
# Works, but NOTHING may follow the \ -- not even a space

x2 = (-b - sqrt(b ** 2 - 4 * a * c)) \
    / (2 * a)

print("x2 (backslash) = ", x2)