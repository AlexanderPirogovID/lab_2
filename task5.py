numbers = list(range(1, 21))
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
increased_numbers = list(map(lambda x: x + 10, even_numbers))
sorted_numbers = sorted(increased_numbers, reverse=True)

print(numbers)
print("четные: ", even_numbers)
print("увеличенные на 10: ", increased_numbers)
print("по убыванию: ", sorted_numbers)