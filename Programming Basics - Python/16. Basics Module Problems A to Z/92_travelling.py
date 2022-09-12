destination = input()

while destination != 'End':
    trip_price = float(input())
    money_saved_current_destination = 0
    while money_saved_current_destination < trip_price:
        saved_amount = float(input())
        money_saved_current_destination += saved_amount
    print(f'Going to {destination}!')
    destination = input()
