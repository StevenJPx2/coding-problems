"""
Problem link: https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050edf/00000000000510ed


GOOGLE KICKSTART - ROUND A PROBLEM 1


Problem

Supervin has a unique calculator. This calculator only has a display, a plus button, and a minus button. 
Currently, the integer N is displayed on the calculator display.

Pressing the plus button increases the current number displayed on the calculator display by 1. 
Similarly, pressing the minus button decreases the current number displayed on the calculator display by 1. 
The calculator does not display any leading zeros. For example, if 100 is displayed on the calculator display, 
pressing the minus button once will cause the calculator to display 99.

Supervin does not like odd digits, because he thinks they are "odd". 
Therefore, he wants to display an integer with only even digits in its decimal representation, using only the 
calculator buttons. Since the calculator is a bit old and the buttons are hard to press, he wants to use 
a minimal number of button presses.

Please help Supervin to determine the minimum number of button presses to make the calculator display an 
integer with no odd digits.


---------------------------

Input

The first line of the input gives the number of test cases, T. T test cases follow. 
Each begins with one line containing an integer N: the integer initially displayed on Supervin's calculator.


---------------------------


Output

For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) 
and y is the minimum number of button presses, as described above.


---------------------------

Limits

1 ≤ T ≤ 100.
Time limit: 20 seconds per test set.
Memory limit: 1GB.

"""

# THOUGHT PROCESS

"""
One way to solve this problem is by converting the input into a string.

So, "2345874249" --> this is an iterable object.

So, we can now check if all digits are even or not, very fast by cross-checking each integer with 2 for divisibility

The whole calculator thing really doesn't matter, that's for show. Number of 1's is equal to the difference b/w the
orig_num and even_num.

Now another thing about +1 and -1 is that it doesn't matter whether we are going up or down cause we're not looking 
at the smallest possible number, smallest difference.


So, if the integer is 3, it can either +1 or -1 to become even, so the function returns 1.
Similarly, 34, smallest difference downwards is 28 (-6), smallest difference upwards 40 (6).
Another example: 2765, smallest difference downwards is 2688 (-77), smallest difference upwards 2800 (35).

So, we see that the difference is different, but the pattern between the numbers are easy enough to figure out.

We work our way in from the left, towards the nearest odd digit. We +/- 1 to it.

e.g. 2345874249, 3 is the nearest odd digit from the left.

+1 --> 2445874249 , replace the rest with 0's, as everything else is dead weight --> 2400000000
-1 --> 2245874249 , replace the rest with 8's, as everything else is dead weight --> 2288888888

Find the difference: +1 : -54,125,751
                     -1 : 56,985,361

+1 is smaller.
"""


def beautiful_integer_generator(n, debug=False):
    str_n = str(n)
    len_n = len(str_n)

    is_even = True

    for index in range(len_n):
        digit = int(str_n[index])
        if digit % 2:
            if digit == 9 and index > 0:
                if debug: print(digit)
                plus_1 = int(f"{int(str_n[:index])+2}0{'0'*((len_n-index)-1)}")
            else:
                plus_1 = int(f"{str_n[:index]}{digit+1}{'0'*((len_n-index)-1)}")
            min_1 = int(f"{str_n[:index]}{digit-1}{'8'*((len_n-index)-1)}")
            is_even = False
            break

    if not is_even:
        if debug: print((plus_1, (plus_1-n)), (min_1, (n-min_1)))
        answer = (plus_1-n) if (plus_1-n) < (n-min_1) else (n-min_1)
    else:
        answer = 0

    if debug:
        print(answer)
        print()

    return answer


def big_for_google():
    iterations = int(input())
    answers = []
    for i in range(iterations):
        n = int(input())
        str_n = str(n)
        len_n = len(str_n)

        is_even = True

        for index in range(len_n):
            digit = int(str_n[index])
            if digit % 2:
                if digit == 9:
                    plus_1 = int(f"{int(str_n[:index])+2}0{'0'*((len_n-index)-1)}")
                else:
                    plus_1 = int(f"{str_n[:index]}{digit+1}{'0'*((len_n-index)-1)}")
                min_1 = int(f"{str_n[:index]}{digit-1}{'8'*((len_n-index)-1)}")
                is_even = False
                break

        if not is_even:
            answer = (plus_1-n) if (plus_1-n) < (n-min_1) else (n-min_1)
        else:
            answer = 0

        answers.append(answer)
    for i in range(len(answers)):
        print(f"Case #{i+1}: {answers[i]}")



if __name__ == "__main__":
    beautiful_integer_generator(13751, 1)
    beautiful_integer_generator(97531, 1)
    beautiful_integer_generator(88892, 1)
    # big_for_google()