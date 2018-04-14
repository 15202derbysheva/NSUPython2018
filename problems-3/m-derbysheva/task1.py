import re
import sys
import math


def skip(iterable, prefix):
    for line in iterable:
        if line.startswith(prefix):
            break


def matching(iterable, prefix, pattern, suffix=""):
    for line in iterable:
        if line.startswith(prefix) and line.endswith(suffix):
            yield int(pattern.search(line).group())


try:
    with open(sys.argv[1]) as file:
        number_pattern = re.compile("[0-9]+\s*(?=usec)")
        sum = 0
        sqr = 0
        count = 0
        skip(file, "open")
        for value in matching(file, "open", number_pattern):
            sum += value
            sqr += value * value
            count += 1

        file.seek(0)
        average = sum / count
        standard_deviation = math.sqrt(sqr / count - average * average)

        print("average {0}\ndeviation {1}".format(average, standard_deviation))
except Exception as e:
    print(e, file=sys.stderr)
