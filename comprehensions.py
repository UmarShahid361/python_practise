numbers = [1, 2]
fruits = ["Apple", "Banana"]
squares = []

# Zip
for fruit, num in zip(fruits, numbers):
    print(f"{fruit} and {num}")
# enumerate
for index, num in enumerate(numbers):
    print(f"Index is {index} and number is {num}")

# Comprehension
squares = [num * num for num in numbers]

temps = [22, 30, 15, 28, 10]
hot_days = [temp for temp in temps if temp > 20]

print(hot_days)

print(squares)

permissions = [True, True, False, True]
check = all(permissions)
check = any(permissions)
print(check)
