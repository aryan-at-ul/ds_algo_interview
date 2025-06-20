"""
Bubble Sort Algorithm Implementation
The methods sorts by comparing 2 elements at a time, start with the entire array
go from 0th elemenet compare it to the next, if they are out of order swap them,
then j goes to next element, jth value will have the largest value of the previous 2 elements
This process is repeated until the larget element is at the end of the array.

In next iteration, we do the same but do not care about the last element. 

Intuition: Buoyancy (not beyonce!, but again to get to the top a bubble has to thank beyonce), the largest bubble will always float to the top first.

"""



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