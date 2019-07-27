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


EDIT 2:

Reason why the depth parameter is so important is because the tree method works depth-first.
Hence, when the iterator back-tracks, it appends the changes to the original history list in the wrong area.

Let me explain it with an example.


The list at depth 3 - [1,1,1], n = 4. 
Since sum of [1,1,1] is 3, it goes further down.

At depth 4: [1,1,1,1] == 4 (!!)

Now, it returns that value and goes to depth 3.

But the list is still - [1,1,1,1]

At depth 3, it has to insert the value here:

[1, 1, 1, 1]
          ^

But because of no depth tracking, it simply appends the value.

i.e, [1, 1, 1, 1, 2] (desired output: [1, 1, 1, 2])

This can be easily solved by simply slicing the list to the depth number:

i.e, ([1, 1, 1, 1]).slice(depth) --> ([1, 1, 1]).append(next_number) --> [1, 1, 1, 2]
"""

# SOLVED!!!
# ADDED DEPTH AS A PARAMETER TO TRACK CHANGES


def tree_method(n=4, steps=[1,2], debug=True, history=[], depth=0):
    
    history = list(history)

    for number in steps:
        history.append(number)
        total_sum = sum(history)
        if total_sum < n:
            if debug: print(history, "<", depth)
            tree_method(n, steps, debug, history, depth+1)
        elif total_sum == n:
            if debug: print(history, "=", depth)
            else: print(history)
        else:
            if debug: print(history, total_sum, ">", depth)
        history = list(history)[:depth]
    
if __name__ == "__main__":
    tree_method(6, [1,3,5])
    tree_method(6, [1,3,5], False)
    # tree_method(debug=False)