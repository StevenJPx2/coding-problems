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


I'll have to use recursion for this.
Somehow I'll have to track the history of numbers.



EDIT:

The above tree did not track 3+3, cause 3 wasn't the root. So that has to be done as well.
"""

# PARTIALLY WORKING

def tree_method(n=4, steps=[1,2], root=0, history=[]):
    
    total_sum = root
    __history = list(history)

    for number in steps:
        total_sum += number
        __history.append(number)
        if total_sum < n:
            tree_method(n, steps, total_sum, __history)
        elif total_sum == n:
            print(__history)
            history = []
            return
        else:
            history = []
            return
    
if __name__ == "__main__":
    tree_method()