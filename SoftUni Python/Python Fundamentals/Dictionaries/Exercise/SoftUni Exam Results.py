def banned(seq, scores):
    user_name = seq[0]

    if user_name in scores:
        del scores[user_name]


def submissions(seq, scores, counter):
    user_name = seq[0]
    language = seq[1]
    points = seq[2]

    if user_name not in scores:
        scores[user_name] = {}
        scores[user_name][language] = points
    else:
        if language not in scores[user_name]:
            scores[user_name][language] = points
        else:
            if int(scores[user_name][language]) < int(points):
                scores[user_name][language] = points
    if language not in counter:
        counter[language] = 1
    else:
        counter[language] += 1

    return scores


def exam(seq):
    counter = {}
    scores = dict()
    while seq != "exam finished":

        seq = seq.split("-")

        if 'banned' in seq:
            banned(seq, scores)

        else:
            submissions(seq, scores, counter)

        seq = input()

    print("Results:")
    for keys in scores:
        for k in scores[keys]:
            print(f"{keys} | {scores[keys][k]}")
    print("Submissions:")
    for k, v in counter.items():
        print(f"{k} - {v}")


sequence = input()
exam(sequence)