needed_experience = float(input())
battles_count = int(input())
gained_experience = 0
experience_gathered = False

for battle in range(1, battles_count + 1):
    current_battle_experience = float(input())
    if battle % 3 == 0:
        current_battle_experience += 0.15 * current_battle_experience
    if battle % 5 == 0:
        current_battle_experience -= 0.10 * current_battle_experience
    if battle % 15 == 0:
        current_battle_experience += 0.05 * current_battle_experience
    gained_experience += current_battle_experience
    if gained_experience >= needed_experience:
        experience_gathered = True
        break

if experience_gathered:
    print(f'Player successfully collected his needed experience for {battle} battles.')
else:
    diff = abs(needed_experience - gained_experience)
    print(f'Player was not able to collect the needed experience, {diff:.2f} more needed. ')

