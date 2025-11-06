print("Welcome to SMIT TechFest!")
print("Event organized by John Angot of APPDAET BTCS0")

try:
    n = int(input("How many participants will register? ").strip())
except:
    n = 0

if n <= 0:
    print("Invalid number of participants.")
    raise SystemExit
