"""
Insertion Sort Algorithm Implementation

Works by building a sorted array one element at a time.
The algorithm iterates through the array, and for each element, it finds the appropriate position in the already sorted part of the array and inserts it there.
The process is repeated until the entire array is sorted.
"""


class InsertionSort:

    def __init__(self,array):
        self.array = array 
        self.sorted = False


    def sort(self):

        n = len(self.array)

        for i in range(len(self.array)):
            j = i
            while j > 0 and self.array[j-1] > self.array[j]: # a sign change in comparision can change the order of sorting
                self.swap(j, j-1)
                j -= 1
        self.sorted = True
        return self.array
                
    def swap(self,i , j):
        self.array[i], self.array[j] = self.array[j], self.array[i]


if __name__ == '__main__':
    arr = [3, 2, 1, 5, 4]
    # arr = [5, 3]
    # arr = [1, 2, 3, 4, 5]
    insertion_sort = InsertionSort(arr)
    print("Original array:", insertion_sort.array)
    print("Is sorted:", insertion_sort.sorted)
    insertion_sort.sort()
    print("Sorted array:", insertion_sort.array)
    print("Is sorted:", insertion_sort.sorted)