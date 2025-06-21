"""
Shell sort implementation in Python.
Shell sort is an optimization of insertion sort that allows the exchange of items that are far apart.


"""

class ShellSort:

    def __init__(self, array):
        self.array = array
        self.sorted = False

    def sort(self):

        n = len(self.array)

        gap = n // 2  # Start with a large gap, then reduce it
        while gap > 0:

            for i in range(gap,n):

                #this will be insertion sort
                j = i
                while j >= gap and self.array[j - gap] > self.array[j]:
                    self.swap(j, j - gap)
                    j -= gap

            gap //= 2  # Reduce the gap for the next iteration
        self.sorted = True
        return self.array
    
    def swap(self, i, j):

        self.array[i], self.array[j] = self.array[j], self.array[i]


if __name__ == '__main__':
    arr = [3, 2, 9, 5, 4, 6, 1 , 8, 7]
    # arr = [5, 3]
    # arr = [1, 2, 3, 4, 5]
    shell_sort = ShellSort(arr)
    print("Original array:", shell_sort.array)
    print("Is sorted:", shell_sort.sorted)
    shell_sort.sort()
    print("Sorted array:", shell_sort.array)
    print("Is sorted:", shell_sort.sorted)