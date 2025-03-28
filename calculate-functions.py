def add_numbers(number1, number2):
    sum = number1 + number2
    return sum

a = 10
b = 20

add_numbers(number1=a, number2=b)
add_numbers(a, b)

c = add_numbers(a, b)
print(f"Die summe von a={a} und b={b} ist {c}.")
d = add_numbers(c, 5)
print(f"diee summe von c={c} und 5 ist {d}.")