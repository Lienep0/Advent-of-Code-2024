# "Putain en fait c'était de la prog dyn"
memo = {}
data = [int(x) for x in open("input.txt").readline().split(" ")]

def score_rec(data, blink_number):
    if blink_number == 0:
        return 1

    if (data, blink_number) in memo:
        return memo[(data, blink_number)]
    
    length = len(str(data))

    if length % 2 == 0:
        current_score = (score_rec(int(str(data)[:length // 2]), blink_number - 1) 
                        + score_rec(int(str(data)[length // 2:]), blink_number - 1))
    elif data == 0:
        current_score = score_rec(1, blink_number - 1)
    else:
        current_score = score_rec(data * 2024, blink_number - 1)
    
    memo[(data, blink_number)] = current_score
    return current_score

def score(data, blink_number):
    s = 0
    for datapoint in data:
        s += score_rec(datapoint, blink_number)
    return s

print(score(data, 75))