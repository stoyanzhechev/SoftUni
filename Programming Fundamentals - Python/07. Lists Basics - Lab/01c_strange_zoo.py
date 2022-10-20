meerkat = []

for _ in range(3):
    meerkat_part = input()
    meerkat.append(meerkat_part)

meerkat[0], meerkat[2] = meerkat[2], meerkat[0]

print(meerkat)
