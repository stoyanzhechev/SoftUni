profit_threshold = float(input())
total_profit = 0
funds_raised = False

command = input()
while command != 'Party!':
    cocktail_name = command
    cocktails_count = int(input())
    cocktail_price = len(command)
    current_profit = cocktails_count * cocktail_price

    if current_profit % 2 != 0:
        current_profit *= 0.75

    total_profit += current_profit

    if total_profit >= profit_threshold:
        funds_raised = True
        break

    command = input()

if funds_raised:
    print("Target acquired.")
else:
    diff = abs(total_profit - profit_threshold)
    print(f"We need {diff:.2f} leva more.")
print(f"Club income - {total_profit:.2f} leva.")




