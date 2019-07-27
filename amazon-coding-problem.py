""" 
Problem from: https://www.dailycodingproblem.com/stackabuse

Sample Programming Interview Question
ASKED BY: AMAZON


There's a staircase with N steps, and you can climb 1 or 2 steps at a time. 
Given N, write a function that returns the number of unique ways you can climb the staircase. 
The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:

- 1, 1, 1, 1
- 2, 1, 1
- 1, 2, 1
- 1, 1, 2
- 2, 2

What if, instead of being able to climb 1 or 2 steps at a time, 
you could climb any number from a set of positive integers X? For example, if X = {1, 3, 5}, 
you could climb 1, 3, or 5 steps at a time. Generalize your function to take in X.


"""

# THOUGHT PROCESS

""" 
Let's suppose:-
steps - [1, 2, 3, 4]
n - 6

It will first see which can reach 6 just by itself (i.e. if 6 is inside)

[1, 2, 3, 4]
 ^
[1, 2, 3, 4]
    ^
[1, 2, 3, 4]
       ^
[1, 2, 3, 4]
          ^


None are.

Now, it will first see which can reach 6 by adding two numbers

First: through 1

[1, 2, 3, 4]
 ^+
[1, 2, 3, 4]
 ^+ ^
[1, 2, 3, 4]
 ^ +   ^
[1, 2, 3, 4]
 ^ +      ^

None by adding to 1.

Second: through 2
[1, 2, 3, 4]
 ^+ ^
[1, 2, 3, 4]
  + ^
[1, 2, 3, 4]
    ^+ ^
[1, 2, 3, 4]
    ^ +   ^

4 and 2 add to 6 – that will be appended to the list
.
.
.


Now, if we will check to see which can reach 6 by adding three numbers,
it will be exponential (or factorial, I'm not sure. Either way, not good.)

So, we don't want to do that.

And we have to do this till 6. Let's try this in the brute_steps function.

One way to optimise it is 
"""

# Brute force method
# trying by hardcoding as much as possible

def brute_steps(n=4, steps=[1, 2]):
    unique_steps = []
    sum = 0

    for i in range(1, n+1):
        ls = []
        sum = 0
        for number in steps:
            sum = number
            for added in steps:
                for iterator in range(i):
                    sum += added


    print(unique_steps)

def smarter_steps(n=4, steps=set([1, 2])):
    unique_steps = {}
    sum = 0
    for i in steps:
        lis = []
        while sum != n:
            sum += i * n
            lis.extend([f"{i}" for _ in range(n)])
            if sum > n:
                old_sum = sum
                sum /= i
                for _ in range(old_sum-sum):
                    lis.remove(i)

        unique_steps[lis] = sum


if __name__ == "__main__":
    brute_steps()