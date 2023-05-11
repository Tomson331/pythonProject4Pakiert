# Dzień 74 Moduły cdn.

# mathematics.py tworzenie modułu o nazwie mathematics
import letters as letters


def add(a, b):
    return a + b

#Jak używać modułów:
# main.py

# Importowanie całego modułu
import mathematics

result = mathematics.add(4, 5)
print(result) # Wypisze: 9

# Importowanie tylko funkcji add
from mathematics import add

result2 = add(7, 3)
print(result2) # Wypisze: 10

# Importowanie modułu pod inną nazwą
import mathematics as mat

result3 = mat.add(1, 2)
print(result3) # Wypisze: 3

# Importowanie funkcji pod inną nazwą
from mathematics import add as d

result4 = d(3, 3)
print(result4) # Wypisze: 6

# Zadanie
# Stwórz moduł o nazwie text, który zawiera następujące funkcje:
#
#     1.small_letters(s): Zmienia wszystkie litery w tekście na małe.
#     2. large_letters(s): Zmienia wszystkie litery w tekście na wielkie

# text.py

def text1 (small letters(s))
def text2 (large letters(s))
    return small letters + large letters

#main.py
import text

result = text.add(small letters, large letters)
print(result)

from text.adding import add



