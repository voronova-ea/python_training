from fixture.orm import ORMFixture
from model.group import Group
from model.contact import Contact
import random

db = ORMFixture(host='127.0.0.1', name='addressbook', user='root', password='')

try:
    l = db.get_groups_for_contact(Contact(id='1057'))
    for item in l:
        print(item)
    print(len(l))
finally:
    pass  # db.destroy()