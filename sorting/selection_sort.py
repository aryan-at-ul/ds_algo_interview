"""
Selection sort is a simple and intuitive sorting algorithm.
It works for finding the minimum element and placing it at the beginning of the array.
first linear search starts at index 0, compares it to all next elements, its its larger than any its saves its index in min_index.
This when performed for all element, we end up with the smallest element. swap that with the first element.
Then we repeat it for all elements - the elements that are already sorted are not considered in the next iterations.
"""


class SelectionSort:

    def __init__(self,array):
        self.array = array
        self.sorted = False


    def sort(self):
        n = len(self.array)

        for i in range(n):
            # finding the min element to put at the beginning
            min_index = i
            for j in range(i +1, n):
                if self.array[i] > self.array[j]:
                    min_index = j
                    
            self.swap(i, min_index)

        self.sorted = True
        return self.array


    def swap(self, i, j):
        self.array[i] , self.array[j] = self.array[j], self.array[i]

if __name__ == '__main__':
    arr = [3, 2, 1, 5, 4]
    # arr = [5, 3]
    # arr = [1, 2, 3, 4, 5]
    selection_sort = SelectionSort(arr)
    print("Original array:", selection_sort.array)
    print("Is sorted:", selection_sort.sorted)
    selection_sort.sort()
    print("Sorted array:", selection_sort.array)
    print("Is sorted:", selection_sort.sorted)
