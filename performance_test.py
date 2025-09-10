import random
import time
from linear_search import linear_search
import matplotlib.pyplot as plt

def measure_time(size):
    arr = [random.randint(1, 1000) for _ in range(size)]
    target = random.choice(arr)
    start_time = time.time()
    linear_search(arr, target)
    end_time = time.time()
    return end_time - start_time

sizes = [10, 100, 1000, 10000]
times = [measure_time(size) for size in sizes]

plt.plot(sizes, times, marker='o')
plt.xlabel("Размер списка")
plt.ylabel("Время выполнения (секунды)")
plt.title("Зависимость времени выполнения от размера списка")
plt.grid(True)
plt.savefig("performance_graph.png")