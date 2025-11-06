print("Welcome to SMIT TechFest!")
print("Event organized by John Angot of APPDAET BTCS0")

try:
    n = int(input("How many participants will register? ").strip())
except:
    n = 0

if n <= 0:
    print("Invalid number of participants.")
    raise SystemExit

participants = []
for _ in range(n):
    name = input("Enter participant name: ").strip()
    track = input("Enter chosen track: ").strip()
    participants.append({"name": name, "track": track})

print("\nRegistered Participants:")
for i, p in enumerate(participants, 1):
    print(f"{i}. {p['name']} - {p['track']}")
