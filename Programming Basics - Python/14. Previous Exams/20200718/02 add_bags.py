luggage_over_20_kg = float(input())
luggage_kg = float(input())
days_count = int(input())
total_bags = int(input())

luggage_price = 0
extra_tex = 0

if luggage_kg > 20:
    luggage_price = luggage_over_20_kg
elif 10 <= luggage_kg <= 20:
    luggage_price = luggage_over_20_kg * 0.50
elif luggage_kg:
    luggage_price = luggage_over_20_kg * 0.20

total_luggage_price = luggage_price * total_bags

surcharge = 0
final_price = 0

if days_count < 7:
    surcharge = 40
    final_price = 1.40 * total_luggage_price
elif days_count <= 30:
    surcharge = 15
    final_price = 1.15 * total_luggage_price
else:
    surcharge = 10
    final_price = 1.10 * total_luggage_price

print(f"The total price of bags is: {final_price:.2f} lv.")