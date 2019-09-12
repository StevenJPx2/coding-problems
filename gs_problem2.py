def sum_prime(n): 
    prime = [True] * (n + 1) 
 
    p = 2
    while p * p <= n: 
        if prime[p]: 
            i = p * 2
            while i <= n: 
                prime[i] = False
                i += p 
        p += 1    
    sum = 0
    for i in range (2, n + 1): 
        if(prime[i] and not (n % i)):
            sum += i 
    return sum

def max_subset_sum(steps, subsets, _sum=[0]):
    tot = 0
    for i in range(steps+1):
        if subsets > 0: 
            tot += i + max_subset_sum(steps, subsets-1, _sum)
        elif tot == 7:
            _sum[0] += 1
    
    print(_sum)
    

array = [1,2,6]
t = sum(sum_prime(i) for i in array) % 10**6
max_subset_sum(t, 2)
