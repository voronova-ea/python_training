# -*- coding: utf-8 -*-
from model.contact import Contact


def test_contact_add(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(Contact(firstname="Homer", middlename="Jay", lastname="Simpson", nickname="Hommy",
                               title="Some", company="NPS", address="Springfield", home="027220", mobile="567890",
                               work="026789", fax="026790", email1="h.simpson@gmail.com", email2="h.simpson@somemail.com",
                               email3="h.simpson@someelsemail.com", homepage="facebook.com", bday="10", bmonth="May",
                               byear="1959", aday="10", amonth="May", ayear="2019", address2="Something", phone2="007",
                               notes="Best friend"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)



def test_empty_contact_add(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(Contact(firstname="", middlename="", lastname="", nickname="", title="", company="",
                               address="", home="", mobile="", work="", fax="", email1="", email2="", email3="",
                               homepage="", bday="", bmonth="-", byear="", aday="", amonth="-", ayear="", address2="",
                               phone2="", notes=""))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
