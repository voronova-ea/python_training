from model.group import Group
import os.path
import random
import string
import json
import getopt
import sys
import re

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/groups.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " " * 10
    return prefix + re.sub("[\\'`<>*]", "", "".join([random.choice(symbols) for _ in range(random.randrange(maxlen))]))


testdata = [Group(name=name, header=header, footer=footer)
            for name in ["", random_string("name", 10)]
            for header in ["", random_string("header", 20)]
            for footer in ["", random_string("footer", 20)]] + \
           [Group(name=random_string("name", 10), header=random_string("header", 20),
                  footer=random_string("footer", 20))
            for _ in range(n)] + \
           [Group(name=random_string("name", 10))] + \
           [Group(header=random_string("header", 20))] + \
           [Group(footer=random_string("footer", 20))]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    out.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2))