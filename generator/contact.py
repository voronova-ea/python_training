from model.contact import Contact
import os.path
import random
import string
import getopt
import jsonpickle
import sys
import re

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " " * 10
    return prefix + re.sub("[:'`<>*]", "", "".join([random.choice(symbols) for _ in range(random.randrange(maxlen))]))


def random_number(maxlen):
    symbols = string.digits + "-()" + " " * 10
    return "".join([random.choice(symbols) for _ in range(random.randrange(maxlen))])


months = ["-", "January", "February", "March", "April", "May", "June", "July",
          "August", "September", "October", "November", "December"]

testdata = [Contact(firstname="", middlename="", lastname="", nickname="", title="", company="",
                    address="", home="", mobile="", work="", fax="", email1="", email2="", email3="",
                    homepage="", bday="", bmonth="-", byear="", aday="", amonth="-", ayear="", address2="",
                    phone2="", notes="")] + \
           [Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 10),
                    lastname=random_string("lastname", 15), nickname=random_string("nickname", 10),
                    title=random_string("title", 20), company=random_string("company", 30),
                    address=random_string("address", 30), home=random_number(11),
                    mobile=random_number(11), work=random_number(11), fax=random_number(11),
                    email1=random_string("email1", 25), email2=random_string("email2", 25),
                    email3=random_string("email3", 25), homepage=random_string("homepage", 25),
                    bday=str(random.randrange(1, 32)), bmonth=str(months[random.randrange(len(months))]),
                    byear=str(random.randrange(3000)), aday=str(random.randrange(1, 32)),
                    amonth=str(months[random.randrange(len(months))]), ayear=str(random.randrange(3000)),
                    address2=random_string("address2", 30), phone2=random_number(11),
                    notes=random_string("notes", 30))
            for _ in range(n)] + \
           [Contact(firstname=random_string("firstname", 20))] + \
           [Contact(lastname=random_string("lastname", 30))] + \
           [Contact(address=random_string("address", 30))]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))