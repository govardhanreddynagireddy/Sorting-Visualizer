# Sorting Algorithm Visualizer (Python)

An interactive **Sorting Algorithm Visualizer** built using **Python, NumPy, and Matplotlib animations**.
This project dynamically visualizes how popular sorting algorithms work step-by-step.

---

##  Features

*  Dynamic selection of sorting algorithms at runtime
*  Real-time bar chart animation using Matplotlib
*  Algorithm logic separated from visualization
*  Optimized Bubble Sort (early stopping)
*  Easy to extend with new algorithms

---

##  Supported Algorithms

| Algorithm      | Time Complexity | Stable | In-Place |
| -------------- | --------------- | ------ | -------- |
| Bubble Sort    | O(n²)           | ✅ Yes  | ✅ Yes    |
| Selection Sort | O(n²)           | ❌ No   | ✅ Yes    |
| Insertion Sort | O(n²)           | ✅ Yes  | ✅ Yes    |

---

##  Demo (How It Works)

1. Run the program
2. Choose a sorting algorithm from the menu:

   ```
   1. Bubble Sort
   2. Selection Sort
   3. Insertion Sort
   ```
3. Watch the algorithm sort the array visually step-by-step

Each bar represents an element in the array, and its height corresponds to its value.

---
## 📦 Requirements

Make sure you have Python 3 installed, then install dependencies:

```bash
pip install numpy matplotlib
```

---

## ▶️ How to Run

```bash
python sorting_visualizer.py
```

---

## 🧠 Project Structure

```text
sorting-visualizer/
│
├── sorting_visualizer.py   # Main program
├── README.md               # Project documentation
```

---

## 💡 Concepts Used

* NumPy random data generation
* Sorting algorithms (Bubble, Selection, Insertion)
* Matplotlib bar charts
* Matplotlib FuncAnimation
* State-based animation design

---

---

##  Future Enhancements

* Add Merge Sort & Quick Sort
* Color-code comparisons and swaps
* GUI version using Tkinter or PyQt
* Export animations as GIF or MP4
* Side-by-side algorithm comparison

---

##  Author

**Govardhan**
Python | Data Structures | Visualization Enthusiast

---

## ⭐ If you like this project

Give it a ⭐ on GitHub and feel free to fork or contribute!
