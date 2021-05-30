import sys

# file = sys.argv[1]
from copy import copy

with open('total eclipse of the heart.txt', 'r+') as scroll:
    scroll = scroll.read()

scroll = scroll.replace('\n', ' \n ').replace('\t', ' \t ')
words = scroll.split(' ')

"""
matrix = scroll.split('\n')
for pl, line in enumerate(matrix):
    matrix[pl] = line.split(' ')
"""


def index(sgmnt: list):
    fulind = []
    keep = []
    for w in sgmnt:
        if w not in fulind:
            fulind.append(w)
        elif w not in keep:
            keep.append(w)
    return keep


def compress(sgmnt: list):
    ind = index(sgmnt)
    for pl, w in enumerate(sgmnt):
        if w in ind:
            sgmnt[pl] = ind.index(w)
    return sgmnt, ind


def decompress(sgmnt: list, ind: list):
    for pl, n in enumerate(sgmnt):
        try:
            int(n)
            sgmnt[pl] = ind[n]
        except ValueError:
            pass
    return sgmnt


def expose(sgmnt):
    call = copy(sgmnt)
    for pl, w in enumerate(call):
        try:
            int(w)
            call[pl] = hex(w)[2:]
        except ValueError:
            pass
    return ' '.join(call)


if __name__ == "__main__":
    comp, ind = compress(words)
    with open('total compress of the heart.txt', 'w+') as scroll:
        scroll = scroll.write(expose(comp))
    output = decompress(comp, ind)
    print(' '.join(output))

# todo: deal more intelligently with \n
#       pack into a binary file (both ind and comp)
#       first byte designate the length of each member of the index.
#       add determination
