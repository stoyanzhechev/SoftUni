hall_rent = int(input())

statues_cost = hall_rent * 0.70
catering_cost = statues_cost * 0.85
sound_cost = catering_cost * 0.50

total_cost = hall_rent + statues_cost + catering_cost + sound_cost

print(f'{total_cost:.2f}')