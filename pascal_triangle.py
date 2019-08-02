"""  
GENERATE PASCAL'S TRIANGLE

      1
     1 1
    1 2 1
   1 3 3 1
  1 4 6 4 1
1 5 10 10 5 1


"""


def f(n, memo={}):
    if n == 0 or n == 1:
        return 1

    elif memo.get(n) != None:
        return memo[n]
    
    else:
        memo[n] = n * f(n-1)
        return memo[n]

c = lambda n, k: f(n)/(f(k)*f(n-k))


def p_t(n):
    CENTER = n*12
    for i in range(n+1):
        s = ""
        for k in range(i+1):
            # print(i, k)
            s += str(int(c(i,k))) + " "
            
        print(s.center(CENTER))

p_t(20)