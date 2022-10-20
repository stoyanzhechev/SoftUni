def status(some_number):
    if some_number == 100:
        return "100% Complete!\n[%%%%%%%%%%]"
    return f"{number}% [{'%' * (number // 10)}{(10 - number // 10) * '.'}]\nStill loading..."


number = int(input())
print(status(number))
