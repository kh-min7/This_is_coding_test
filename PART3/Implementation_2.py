s = input()

alphabet = []
number = 0

for i in s:
    if 'A' <= i <= 'z':
        alphabet.append(i)
    elif '0' <= i <= '9':
        number += int(i)

alphabet.sort()

if number != 0:
    alphabet.append(str(number))

for i in alphabet:
    print(i, end='')
    # join 함수 사용법 익히기