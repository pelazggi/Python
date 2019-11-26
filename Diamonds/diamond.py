# Програма, която прочита от конзолата цяло число n(1 < = n < = 100) 
# и чертае диамант в този вид:

# n =4    -**-   n = 3  -*-
#         *--*          *-*
#         -**-          -*-
# Разделяме диаманта на две половини,които са огледални.
# Дефинираме си две променливи (pos1 u pos2), които показват позицията на звездата.
# Броят на нечетните редове е равен на n, а на четните е n-1.

n = int(input('Enter number from 1 to 100:'))

if (n == 1):
    print("*")
elif (n == 2):
    print("**")
else:
    if (n % 2 == 0): #при четни числа
        pos1, pos2 = n // 2, n // 2 + 1 #позиции на звездичката
    else:
        pos1, pos2 = (n + 1) // 2, (n + 1) // 2 # при нечетни числа
    total_row = n - (1 - n % 2) 
for row in range (total_row // 2):
    for col in range (1, n + 1):
        if (col == pos1 or col == pos2):
            print('*', end='')
        else:
            print('-', end='')
    print()
    pos1 -= 1
    pos2 += 1

# втората половина от диаманта

for row in range (total_row - total_row // 2): 
    for col in range (1, n + 1):
        if (col == pos1 or col == pos2):
            print('*', end='')
        else:
            print('-', end='')
    print()
    pos1 += 1
    pos2 -= 1
