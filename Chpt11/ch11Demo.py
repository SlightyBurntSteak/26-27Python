#Variables, Arithmetic, and importing Modules

# Demo 1 - Variables and Assignment
def demo1_variables():
    # Assigning values to variables
    CAN_VOLUME = 0.355
    BOTTLE_VOLUME = 2.0

    cansPerPack = 6
    packVolume = cansPerPack * CAN_VOLUME
    print("Six-pack volume is:", packVolume, "liters.")
    print("Two-liter bottle volume is:", BOTTLE_VOLUME, "liters.")

demo1_variables()

# = means "is set to" or "gets"

print("===============")
lives = 3
print("Starting lives:", lives)
lives = lives + 2
print("Lives remaning:", lives)

#------------------------------
# Demo 3 -Operators and Precedence (11.2)
#------------------------------

print("\n\nOperators and Precedence")

def demo3_operators():
    a = 10
    b = 4
    print("a + b / 2 =", a + b / 2) # 12.0 (division first)
    print("(a + b) / 2 =", (a + b) / 2) # 7.0 (parentheses first)
    print("10 - 2 - 3 =", 10 - 2 - 3) # 5 (left to right)
    print("7 + 4.0 =", 7 + 4.0) # 11.0 (int + float = float)

    # Powers
    print("10 * 2 ** 3 =", 10 * 2 ** 3) # 10 * (2 ** 3) = 10 * 8 = 80
    print("2 ** 3 ** 2 =", 2 ** 3 ** 2) # 2 ** (3 ** 2) = 2 ** 9 = 512 

    # Comparison Interest: balance * (1 + rate/100) ** years
    balance = 1000.0
    rate = 5.0
    years = 10
    future = balance * (1 + rate/100) ** years
    print("Future value: ", future)

demo3_operators()


# Demo 4 - Floor Division and modulus 
print("\n\nFloor Division & Modulus")

def demo4_floor_and_mod():
    print("17 / 5 =", 17 / 5) # 3.4
    print("17 // 5 =", 17 // 5) # 3
    print("17 % 5 =", 17 % 5) # 2

demo4_floor_and_mod()


