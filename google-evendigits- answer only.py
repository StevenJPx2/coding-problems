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
                plus_1 = int(f"{str_n[:index]}{digit+1}"+"0"*((len_n-index)-1))
                min_1 = int(f"{str_n[:index]}{digit-1}"+"8"*((len_n-index)-1))
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
    big_for_google()