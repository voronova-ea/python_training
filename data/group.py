from model.group import Group
import random
import string
import re


constant = [
    Group(name="name1", header="header1", footer="footer1"),
    Group(name="name2", header="header2", footer="footer2")
]


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " " * 10
    return prefix + re.sub("[\\'`<>*]", "", "".join([random.choice(symbols) for _ in range(random.randrange(maxlen))]))


testdata = [Group(name=name, header=header, footer=footer)
            for name in ["", random_string("name", 10)]
            for header in ["", random_string("header", 20)]
            for footer in ["", random_string("footer", 20)]] + \
           [Group(name=random_string("name", 10), header=random_string("header", 20),
                  footer=random_string("footer", 20))
            for _ in range(4)] + \
           [Group(name=random_string("name", 10))] + \
           [Group(header=random_string("header", 20))] + \
           [Group(footer=random_string("footer", 20))]