actor_name = input()
academy_award = float(input())
jury_count = int(input())

total_award = academy_award

for current_jury_member in range(jury_count):
    jury_member_name = input()
    jury_member_award = float(input())
    total_award += len(jury_member_name) * jury_member_award / 2

    if total_award > 1250.5:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {total_award:.1f}!")
        break

if total_award < 1250.5:
    diff = 1250.5 - total_award
    print(f"Sorry, {actor_name} you need {diff:.1f} more!")

