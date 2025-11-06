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

tracks = sorted({p["track"] for p in participants if p["track"]})
print("\nTracks offered in this event:")
print(", ".join(tracks) if tracks else "")
if len(tracks) < 2:
    print("\nNot enough variety in tracks.")

seen = set()
dups = set()
for p in participants:
    nm = p["name"]
    if nm in seen:
        dups.add(nm)
    else:
        seen.add(nm)

if dups:
    for d in sorted(dups):
        print(f"\nDuplicate name found: {d}")
else:
    print("\nNo duplicate names.")

summary = {}
for p in participants:
    t = p["track"]
    summary[t] = summary.get(t, 0) + 1

print("\nParticipants per track:")
for t in sorted(summary):
    print(f"{t}: {summary[t]}")
