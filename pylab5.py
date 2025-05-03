numbers = list(range(1, 21))
# фильтурем четные числа
filtered = list(filter(lambda x: x % 2 == 0, numbers))

#увел на 10

mapped = list(map(lambda x: x + 10, filtered))
# сортировка по убыванию

sorted_nums = sorted(mapped, reverse=True)

print("Четные числа +10 по убыванию:")
print(sorted_nums)
