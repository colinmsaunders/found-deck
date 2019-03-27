import random, sys


def do_sim(starting, find_prob, avg_find):
    d = {}
    for i in range(starting):
        d[i] = (1, 0)
    n = 0
    while len(d) < 52:
        found_any = random.random()
        n += 1
        if found_any > find_prob:
            continue
        num_found = 1
        num_found += int(random.random() * (avg_find - 1))
        k = None
        for i in range(num_found):
            k = random.randint(0, 51)
            if None == d.get(k):
                d[k] = (1, n)
                break
    return n, d


def many_sim(n, starting, find_prob, avg_find):
    t = 0
    for i in range(n):
        x = do_sim(starting, find_prob, avg_find)
        t += x[0]
    return t / float(n)


if __name__ == '__main__':
    c = sys.argv[1]
    if 'days' == c:
        starting = int(sys.argv[2])
        find_prob = float(sys.argv[3])
        avg_find = float(sys.argv[4])
        x = do_sim(starting, find_prob, avg_find)
        k = map(lambda z: z[1], x[1].values())
        k.sort()
        start = k[0]
        for i in k:
            j = i - start
            print '%d days\t%.2f months\t%.2f years' % (j, j / 30.0, j / 365.25)
    if 'sim' == c:
        n = int(sys.argv[2])
        starting = int(sys.argv[3])
        find_prob = float(sys.argv[4])
        avg_find = float(sys.argv[5])
        x = many_sim(n, starting, find_prob, avg_find)
        print '%d days\t%.2f months\t%.2f years' % (x, x / 30.0, x / 365.25)
