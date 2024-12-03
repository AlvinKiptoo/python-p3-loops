#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    countdown = 10
    while countdown > 0:
        print(countdown)
        countdown -= 1
    print("Happy New Year!")

def square_integers(int_list):
    # code goes here!
    return [x ** 2 for x in int_list]

def fizzbuzz(num):
    # code goes here!
    for num in range(100):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)
