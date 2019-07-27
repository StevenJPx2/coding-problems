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

One way to optimise it is by reducing the number of numbers it has to add by the end.

So if there is a list of [2,3,4],
and it has to add to 6, we do not need the iterator to add 6 numbers out of the gate
cause we know that the minimum (2) only needs to be added three times to itself to get a 
total of 6. And three numbers to be added is the maximum we'll see for this is list.

So for this, we can put a variable min_to_succeed, where the N (6) is integer-divided by the smallest
number in the list (2) and the list only has to work up to this number.


This problem, however, just softens the blow of the exponential work the iterator has to otherwise do.

Another way is to memoise. Since we are working our way towards adding more numbers,
we can save the numbers that are added already.

In that case, I feel that it acts like a tree of sorts.


steps - [2, 3, 4]
n - 6



                            (2,2)
             /                |            \\
          (2,4)             (3,5)         (4,6)
        /   |  \\         /   |  \\         ^ 
     (2,6)(3,7)(4,8)   (2,7)(3,8)(4,9)  
       ^    X    X       X    X    X   


So, in this, smallest number is the root.
In the tuple, (number_selected, total_sum) <-- is what it represents.

Then, 
if total_sum < n:
    add_with_steps()
elif total_sum == n:
    mark_history(tuple)
else:
    cut_off()

This might be the most cost-effective and fruitful one so far.

Let's see what I can do.

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