import math


def occurrences(lst):
    out = {}
    for c in lst:
        if c in out:
            out[c] += 1
        else:
            out[c] = 1
    return out


def frequencies(lst):
    occs = occurrences(lst)
    all_occ = sum(occs.values())
    for k in occs:
        occs[k] /= all_occ
    return occs


def entropy(freqs, n):
    out = 0
    for v in freqs.values():
        out += v * (math.log2(v))
    return - out / n


def r(entr):
    return 1 - (entr / math.log2(32))


def sort(d):
    return sorted(d.items(), key=lambda x: x[0])


def chunks(lst, n, shift=None):
    if shift is None:
        shift = n
    for i in range(0, len(lst), shift):
        out = lst[i:i + n]
        if len(out) != n:
            break
        yield out


def windows(lst, n): return chunks(lst, n, 1)


def to_matrix(freqs):
    f = list(sorted(set(map(lambda x: x[0], freqs.keys()))))

    s = list(sorted(set(map(lambda x: x[1], freqs.keys()))))
    size_f = len(f)
    size_s = len(s)
    out = [['    0  ' for _ in range(0, size_s + 1)] for _ in range(0, size_f + 1)]
    out[0][0] = ' - '
    for i in range(1, size_f + 1):
        out[i][0] = f' {f[i - 1]}  '
    for j in range(1, size_s + 1):
        out[0][j] = f'     {s[j - 1]} '

    for i in range(1, size_f + 1):
        for j in range(1, size_s + 1):
            k = f'{f[i - 1]}{s[j - 1]}'
            if k in freqs:
                out[i][j] = " {:.4f}".format(freqs[k] * 100)
    return out


def print_matrix(m):
    for r in m:
        for e in r:
            print(e, end='')
        print()


def all(path):
    f = open(path, 'r')
    text = f.read()
    f.close()
    f1 = frequencies(text)
    f2 = frequencies(chunks(text, 2))
    f2o = frequencies(windows(text, 2))
    h1 = entropy(f1, 1)
    h2 = entropy(f2, 2)
    h2o = entropy(f2o, 2)
    print("Frequencies of letters:")
    for (k,v) in sort(f1):
        print(f'{k} : {v*100}')
    print("Frequencies of bigrams:")
    print_matrix(to_matrix(f2))
    print("Frequencies of bigrams(overlapped):")
    print_matrix(to_matrix(f2o))
    print(f'H1 = {h1}')
    print(f'H2 = {h2}')
    print(f'H2(overlapped) = {h2o}')
    print(f'R1 = {r(h1)}')
    print(f'R2 = {r(h2)}')
    print(f'R2(overlapped) = {r(h2o)}')


if __name__ == '__main__':
    all('blindsight_with_spaces')
    all('blindsight_without_spaces')
