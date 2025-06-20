import random


class BogoSort:
    def __init__(self, array):
        self.array = array
        self.sorted = False

    def sort(self):
        while not self.is_sorted():
            print("suffline to sort")
            self.shuffle()

        self.sorted = True
        return self.array

    def is_sorted(self):

        for i in range(len(self.array)-1):
            if self.array[i] > self.array[i+1]:
                return False
        return True
    
    # Fisher Yates shuffle algorithm: https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle O(n) shuffling
    def shuffle(self):
        for i in range(len(self.array)-2,-1,-1):  # corner case, i = -1
            print("Shuffling: ", self.array)
            j = random.randint(0, i+1)
            self.array[i],self.array[j] = self.array[j], self.array[i]

    
if __name__ == '__main__':
    arr = [3, 2, 1, 5, 4]
    # arr = [5,3]
    bogo_sort = BogoSort(arr)
    print("Original array:", bogo_sort.array)
    print("Is sorted:", bogo_sort.is_sorted())
    sorted_arr = bogo_sort.sort()
    print("Sorted array:", sorted_arr)
    print("Is sorted:", bogo_sort.is_sorted())