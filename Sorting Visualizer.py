import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
#  SORTING ALGORITHMS 
def bubble_sort_states(arr):
    a = arr.copy()
    n = len(a)
    states = [a.copy()]
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                states.append(a.copy())
                swapped = True
        if not swapped:
            break
    return states
def selection_sort_states(arr):
    a = arr.copy()
    n = len(a)
    states = [a.copy()]

    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
        states.append(a.copy())
    return states
def insertion_sort_states(arr):
    a = arr.copy()
    n = len(a)
    states = [a.copy()]

    for i in range(1, n):
        j = i
        while j > 0 and a[j - 1] > a[j]:
            a[j - 1], a[j] = a[j], a[j - 1]
            states.append(a.copy())
            j -= 1
    return states
# DYNAMIC ALGORITHM SELECTION 
print("Choose Sorting Algorithm:")
print("1. Bubble Sort")
print("2. Selection Sort")
print("3. Insertion Sort")

choice = int(input("Enter choice (1/2/3): "))
np.random.seed(42)
n = 30
arr = np.random.randint(1, 100, size=n)
if choice == 1:
    states = bubble_sort_states(arr)
    title = "Bubble Sort Animation"
elif choice == 2:
    states = selection_sort_states(arr)
    title = "Selection Sort Animation"
elif choice == 3:
    states = insertion_sort_states(arr)
    title = "Insertion Sort Animation"
else:
    raise ValueError("Invalid choice!")
print(f"{title} | Total Frames: {len(states)}")
# ANIMATION 
fig, ax = plt.subplots(figsize=(12, 6))
bars = ax.bar(range(n), states[0])
ax.set_xlabel("Index")
ax.set_ylabel("Value")
ax.set_ylim(0, max(arr) * 1.1)
speed = 150  
# animation speed (ms)
def update(frame):
    for bar, height in zip(bars, states[frame]):
        bar.set_height(height)
    ax.set_title(f"{title} — Step {frame}/{len(states)-1}")
    return bars
anim = animation.FuncAnimation(  fig,  update, frames=len(states),interval=speed,  repeat=False)
plt.show()

