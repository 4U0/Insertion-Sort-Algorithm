import matplotlib.pyplot as plt
import numpy as np
import time

def insertion_sort_visual(array):
    fig, ax = plt.subplots()
    ax.set_title("Insertion Sort graph")
    bars = ax.bar(range(len(array)), array, align="center")

    def update_bars(array, color='blue'):
        for bar, val in zip(bars, array):
            bar.set_height(val)
            bar.set_color(color)
        plt.pause(0.1)

    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
            update_bars(array, color='red')
        array[j + 1] = key
        update_bars(array, color='blue')

    update_bars(array, color='green')
    plt.show()

if __name__ == "__main__":
    np.random.seed(0)
    array = np.random.randint(0, 50, 20)
    insertion_sort_visual(array)
