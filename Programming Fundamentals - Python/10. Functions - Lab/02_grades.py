grade = float(input())
assessment = ''

if grade <= 2.99:
    assessment = 'Fail'
elif grade <= 3.49:
    assessment = 'Poor'
elif grade <= 4.49:
    assessment = 'Good'
elif grade <= 5.49:
    assessment = 'Very Good'
elif grade <= 6.00:
    assessment = 'Excellent'

print(assessment)
