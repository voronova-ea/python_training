from model.contact import Contact
import random
import string
import re

constant = [Contact(firstname="firstname1", middlename="middlename1", lastname="lastname1", nickname="nickname1",
                    title="title1", company="company1", address="address1_1", home="11111", mobile="111111111",
                    work="111111", fax="11111", email1="email1@1", email2="email2@1", email3="email3@1",
                    homepage="homepage1", bday="1", bmonth="January", byear="1111", aday="1", amonth="January",
                    ayear="1110", address2="address2_1", phone2="1111111", notes="notes1"),
            Contact(firstname="firstname2", middlename="middlename2", lastname="lastname2", nickname="nickname2",
                    mobile="222222")
            ]


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " " * 10
    return prefix + re.sub("[:'`<>]", "", "".join([random.choice(symbols) for _ in range(random.randrange(maxlen))]))


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
            for _ in range(5)] + \
           [Contact(firstname=random_string("firstname", 10))] + \
           [Contact(lastname=random_string("lastname", 15))] + \
           [Contact(address=random_string("address", 30))]