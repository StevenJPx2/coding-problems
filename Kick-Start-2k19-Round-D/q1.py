from os import path
import random

def xor_sum(array):
    x_sum = 0b000000000000
    for i in array:
        x_sum ^= i
    
    return bin(x_sum)[2:]

def is_xor_even(array):
    
    xor_ans = xor_sum(array)
    d_xor = {'0':0, '1':0}
    for i in xor_ans:
        d_xor[i] += 1

    return True if not d_xor['1'] % 2 else False

def split_sub(A, N):
    sub_intervals = []
    for i in range(N):
        for j in range(i+1, N+1):
            sub_intervals.append(A[i:j])

    return sub_intervals

def ret_max_sub(A, N, debug=False):

    xor_intervals = []

    for i in split_sub(A, N):
        if is_xor_even(i): xor_intervals.append(i)

    maxed = max(xor_intervals, key=lambda x: len(x))

    if debug:
        print(xor_intervals)
        print(maxed, len(maxed))

    return str(len(maxed))


def main():
    T = int(input())

    for case in range(T):
        N, Q = list(map(int, input().split()))

        A = list(map(int, input().split()))

        modified_sub_max = []

        for _ in range(Q):
            P, V = list(map(int, input().split()))
            A[P] = V

            modified_sub_max.append(less_brute_xor(A, N))
        
        print(f"Case #{case+1}: {' '.join(modified_sub_max)}")

def less_brute_xor(A, N):
    max_even = (0,0)
    cache = [0 for _ in range(N+1)]
    for i in range(N):
        _cache = list(cache)
        for j in range(i, N):
            _cache[j+1] = _cache[j]^A[j]
            even = sum(int(i) for i in bin(_cache[j+1])[2:])
            if all((j+1 >= max_even[0], even >= max_even[1], not even % 2)): max_even = (j+1, even)
    return str(max_even[0])

def generate_dataset(N, Q, T=100, Ai=1024, Vi=1024):

    print("Generating dataset...\n\n")

    filename = f"{path.realpath(__file__)[:-3]}_in.in"
    with open(filename, "w") as f:
        f.write(str(T)+"\n")
        for _ in range(T):
            _N, _Q = random.randint(1,N), random.randint(1,Q)
            array = " ".join([str(random.randrange(Ai)) for _ in range(_N)])
            
            f.write(f"{_N} {_Q}\n{array}\n")
            for __ in range(_Q):
                Pi = random.randrange(_N)
                _Vi = random.randrange(Vi)
                f.write(f"{Pi} {_Vi}\n")

    print("Generated!")
        

if __name__ == "__main__":
    # generate_dataset(10, 2, 2)
    # generate_dataset(100, 100)
    main()



    