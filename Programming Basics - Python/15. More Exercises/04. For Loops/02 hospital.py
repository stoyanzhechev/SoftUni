# (Judge 60/100)

period_days = int(input())
doctors_count = 7

treated_patients = 0
untreated_patients = 0

for days in range(1, period_days + 1):
    patients_count = int(input())

    if days % 3 == 0:
        doctors_count += 1

    if doctors_count >= patients_count:
        treated_patients += patients_count
    else:
        treated_patients += doctors_count
        untreated_patients += (patients_count - doctors_count)

print(f"Treated patients: {treated_patients}.")
print(f"Untreated patients: {untreated_patients}.")



