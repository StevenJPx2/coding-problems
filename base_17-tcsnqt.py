from math import pow

"""

BASE 17 PROBLEM
__________________

Convert a base-17 number into an integer number.
That means, (A -> 10, B -> 11, C -> 12, ..., G -> 16)

For example,

Input: 1A
Output: 27

Input: 1BDE3
Output: 141562

"""

"""
EXPLANATION:
______________

What we need is a base-17 number. 

Let us see how base-10 (decimal) numbers work first in order to understand this.

Let us take this number for instance: 12345


1   2   3   4   5
^   ^   ^   ^   ^
5   4   3   2   1st position.

Based on which position it is on, each digit is incremented on to the number.

Therefore,

12345 = 1*10^4 + 2*10^3 + 3*10^2 + 4*10^1 + 5*10^0

That is simple enough.

There is another property about base-10 numbers: they use 10 unique numerals:

0  1  2  3  4  5  6  7  8  9

Octet (base-8) have eight numbers:

0  1  2  3  4  5  6  7

and so on.


This means that base-17 will possess two properties:

1) Each digit is multiplied by a power of 17
2) Base-17 numbers consist of 17 unique numerals:
   0  1  2  3  4  5  6  7  8  9  A  B  C  D  E  F  G

   The letters represent the numbers greater than 9 respectively.


All we have to do to convert base-17 to integer numbers is by converting
the numerals to base-17 and then multiply it by the power of 17 based on its index.


HOW TO CODE IT:
________________

First we retrieve the input as a string. This way we can keep track of the
position of each digit. 

s <- '1A'

However, there is a small problem. Since, strings are accessed from left-to-right,
the most significant digit (1) of the number will be index 0 and the least significant
digit (A) of the number will be the last index.

s <-   '1'    'A'
        ^      ^
        0      1th index

This is not what we want, because numbers start from the right-hand side.
This can be easily fixed, however by reversing the string.


s_rev <-   'A'    '1'
            ^      ^
            0      1th index



Now, we're back in business. All we have to do now is, based on the digit and it's position,
we multiply the digit with 17 to the power of it's position.


int_num <- 'A' * 17^0  +  1 * 17^1


Oops! Looks like we need to convert the letters into the base-17 numbers.
That is easy enough. We can make a lookup table for that, or a bunch of if or switch
statements for each letter would suffice.


int_num <- 10 * 17^0  +  1 * 17^1
int_num <- 10 + 17 <- 27

"""

base_17_num = str(input())
num_rev = base_17_num[::-1] # reversing the number
l = {'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15, 'G':16}

int_num = 0

for index in range(len(num_rev)):
    char = num_rev[index]
    if char.isdigit():
        int_num += int(char) * pow(17, index) # or just int(char) * (17 ** index)
    else:
        int_num += l[char] * pow(17, index)

    # shorter version
    
    # char = num_rev[index]
    # int_num += int(char) * pow(17, index) if char.isdigit() else l[char] * pow(17, index)

print(int(int_num))

