prizes = {
    (2, True): 3,
    (3, False): 5,
    (3, True): 8,
    (4, False): 22,
    (4, True): 218,
    (5, False): 1201,
    (5, True): 35722,
    (6, False): 1_000_000,

}
k = int(input())
for i in range(k):
    correct_numbers = input().split(" ")
    correct_numbers = [int(i) for i in correct_numbers]
    numbers = correct_numbers[:-1]
    extra_number = correct_numbers[-1]
    attemps = int(input())
    profit = 0
    for x in range(attemps):
        attempt = input().split(" ")
        attempt = [int(i) for i in attempt]
        correct = 0
        extra = False
        for a in attempt:
            if a in numbers:
                correct += 1
            elif a == extra_number:
                extra = True
        result = (correct, extra)
        if result in prizes:
            profit += prizes[result]
    print("{} {}".format(i + 1, profit))
