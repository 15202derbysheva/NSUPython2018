import heapq
import re
import sys


def skip(iterable, prefix):
    for line in iterable:
        if line.startswith(prefix):
            break


def matching(iterable, prefix, pattern, suffix=""):
    for line in iterable:
        if line.startswith(prefix) and line.endswith(suffix):
            yield int(pattern.search(line).group())


try:
    file = open(sys.argv[1])
    number_pattern = re.compile("[0-9]+\s*(?=usec)")
    sum = 0
    count = 0
    skip(file, "open")
    for value in matching(file, "open", number_pattern):
        sum += value
        count += 1

    file.seek(0)
    average = sum / count
    top = []
    skip(file, "open")
    for value in matching(file, "open", number_pattern):
        if len(top) < count / 10:
            heapq.heappush(top, value)
        else:
            heapq.heappushpop(top, value)

    print("average {0}\ntop decile {1}".format(average, heapq.nsmallest(1, top)[0]))
except Exception as e:
    print(e, file=sys.stderr)
