heritage_money = float(input())
end_year = int(input())
age = 17

for year in range(1800, end_year + 1):
    age += 1
    if year % 2 == 0:
        heritage_money -= 12000
    else:
        heritage_money -= (12000 + 50 * age)

if heritage_money >= 0:
    print(f"Yes! He will live a carefree life and will have {heritage_money:.2f} dollars left.")
else:
    print(f"He will need {abs(heritage_money):.2f} dollars to survive.")
