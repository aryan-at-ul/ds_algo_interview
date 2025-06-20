



class BubbleSort:

    def __init__(self, array):
        self.array = array
        self.sorted = False


    def sort(self):

        n = len(self.array)

        for i in range(n):
            for j in range(0, n - i -1):
                if self.array[j] > self.array[j+1]:
                    self.swap(j, j+1)

        self.sorted = True
        return self.array

    def swap(self, i, j):
        self.array[i], self.array[j] = self.array[j],self.array[i]


if __name__ == '__main__':

    arr = [3, 2, 1, 5, 4]
    # arr = [5, 3]
    # arr = [1, 2, 3, 4, 5]
    bubble_sort = BubbleSort(arr)
    print("Original array:", bubble_sort.array)
    print("Is sorted:", bubble_sort.sorted)
    bubble_sort.sort()
    print("Sorted array:", bubble_sort.array)
    print("Is sorted:", bubble_sort.sorted)