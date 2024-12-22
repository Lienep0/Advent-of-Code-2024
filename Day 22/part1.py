def mix(n, s):
    return n ^ s

def prune(n):
    return n % 16777216

def op1(n):
    return prune(mix(n * 64, n))

def op2(n):
    return prune(mix(n // 32, n))

def op3(n):
    return prune(mix(n * 2048, n))

def find_secret(seed, iterations = 1):
    for _ in range(iterations):
        seed = op3(op2(op1(seed)))
    return seed

if __name__ == "__main__":
    with open("input.txt", "r") as file:
        numbers = [int(line.strip()) for line in file]

    print(sum([find_secret(n, 2000) for n in numbers]))