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
    
