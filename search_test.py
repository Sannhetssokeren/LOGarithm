import random
from linear_search import linear_search

random_list = [random.randint(1, 1000) for _ in range(100)]

test_values = [random.choice(random_list), 9999]
results = {}

for value in test_values:
    index = linear_search(random_list, value)
    results[value] = index

with open("search_results.txt", "w") as file:
    for value, index in results.items():
        file.write(f"Значение {value}: Индекс {index}\n")