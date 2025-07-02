"""
FizzBuzz is a classic programming challenge that involves printing numbers from 1 to n, but with a twist:
- For multiples of 3, print "Fizz" instead of the number.
- For multiples of 5, print "Buzz" instead of the number.
- For multiples of both 3 and 5, print "FizzBuzz".

"""


class FizzBuzz:

    def __init__(self, n):
        self.n = n
        # self.result = [] # this could be used to store all upto 15, and then its just 15 modulo if 0 then fizzbuzz else # fizz or buzz or number
        self.fizz = "Fizz"
        self.buzz = "Buzz"
        self.fizzbuzz = "FizzBuzz"


    def generate(self):
        for i in range(1,self.n+1):
            if i % 3 == 0 and i % 5 ==0:
                print(self.fizzbuzz)

            elif i % 3 == 0:
                print(self.fizz)

            elif i % 5 == 0:
                print(self.buzz)
            else:
                print(i)



if __name__ == '__main__':
    n = 100  
    fizzbuzz = FizzBuzz(n)
    fizzbuzz.generate()
    # Output will be printed directly to the console        
