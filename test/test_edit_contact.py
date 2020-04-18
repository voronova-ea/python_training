from model.contact import Contact
from random import randrange


def test_contact_edit_all_fields(app):
    app.contact.check(Contact(firstname="", middlename="", lastname="", nickname="", title="", company="",
                              address="", home="", mobile="", work="", fax="", email1="", email2="", email3="",
                              homepage="", bday="", bmonth="-", byear="", aday="", amonth="-", ayear="", address2="",
                              phone2="", notes=""))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="New Homer", middlename="New Jay", lastname="New Simpson",
                      nickname="New Hommy", title="New Some", company="New NPS",
                      address="New Springfield", home="09", mobile="09", work="09",
                      fax="09", email1="new_h.simpson@gmail.com",
                      email2="new_h.simpson@somemail.com",
                      email3="new_h.simpson@someelsemail.com", homepage="new_facebook.com",
                      bday="1", bmonth="June", byear="1999", aday="1", amonth="June", ayear="2029",
                      address2="New Something", phone2="070", notes="Best friend")
    contact.id = old_contacts[index].id
    app.contact.edit_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_contact_edit_all_fields_empty(app):
    app.contact.check(Contact(firstname="Homer", middlename="Jay", lastname="Simpson", nickname="Hommy",
                              title="Some", company="NPS", address="Springfield", home="027220", mobile="567890",
                              work="026789", fax="026790", email1="h.simpson@gmail.com",
                              email2="h.simpson@somemail.com",
                              email3="h.simpson@someelsemail.com", homepage="facebook.com", bday="10",
                              bmonth="May",
                              byear="1959", aday="10", amonth="May", ayear="2019", address2="Something",
                              phone2="070",
                              notes="Best friend"))
    old_contacts = app.contact.get_contact_list()
    app.contact.edit_first_contact(Contact(firstname="", middlename="", lastname="", nickname="", title="", company="",
                                           address="", home="", mobile="", work="", fax="", email1="", email2="",
                                           email3="", homepage="", bday="-", bmonth="-", byear="", aday="-", amonth="-",
                                           ayear="", address2="", phone2="", notes=""))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_contact_edit_firstname(app):
    app.contact.check(Contact(firstname="Homer"))
    old_contacts = app.contact.get_contact_list()
    app.contact.edit_first_contact(Contact(firstname="New Homer"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_contact_edit_middlename(app):
    app.contact.check(Contact(middlename="Jay"))
    old_contacts = app.contact.get_contact_list()
    app.contact.edit_first_contact(Contact(middlename="New Jay"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_contact_edit_lastname(app):
    app.contact.check(Contact(lastname=""))
    old_contacts = app.contact.get_contact_list()
    app.contact.edit_first_contact(Contact(lastname="New Simpson"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_contact_edit_nickname(app):
    app.contact.check(Contact(nickname="Hommy"))
    old_contacts = app.contact.get_contact_list()
    app.contact.edit_first_contact(Contact(nickname="New Hommy"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_contact_edit_title(app):
    app.contact.check(Contact(title=""))
    old_contacts = app.contact.get_contact_list()
    app.contact.edit_first_contact(Contact(title="New Some"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_contact_edit_company(app):
    app.contact.check(Contact(company="NPS"))
    old_contacts = app.contact.get_contact_list()
    app.contact.edit_first_contact(Contact(company="New NPS"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_contact_edit_address(app):
    app.contact.check(Contact(address="Springfield"))
    old_contacts = app.contact.get_contact_list()
    app.contact.edit_first_contact(Contact(address="New Springfield"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_contact_edit_home(app):
    app.contact.check(Contact(home=""))
    old_contacts = app.contact.get_contact_list()
    app.contact.edit_first_contact(Contact(home="09"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_contact_edit_mobile(app):
    app.contact.check(Contact(mobile="567890"))
    old_contacts = app.contact.get_contact_list()
    app.contact.edit_first_contact(Contact(mobile="09"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_contact_edit_work(app):
    app.contact.check(Contact(work="026789"))
    old_contacts = app.contact.get_contact_list()
    app.contact.edit_first_contact(Contact(work="09"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_contact_edit_fax(app):
    app.contact.check(Contact(fax=""))
    old_contacts = app.contact.get_contact_list()
    app.contact.edit_first_contact(Contact(fax="09"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_contact_edit_email1(app):
    app.contact.check(Contact(email1="h.simpson@gmail.com"))
    old_contacts = app.contact.get_contact_list()
    app.contact.edit_first_contact(Contact(email1="new_h.simpson@gmail.com"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_contact_edit_email2(app):
    app.contact.check(Contact(email2="h.simpson@somemail.com"))
    old_contacts = app.contact.get_contact_list()
    app.contact.edit_first_contact(Contact(email2="new_h.simpson@somemail.com"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_contact_edit_email3(app):
    app.contact.check(Contact(email3="h.simpson@someelsemail.com"))
    old_contacts = app.contact.get_contact_list()
    app.contact.edit_first_contact(Contact(email3="new_h.simpson@someelsemail.com"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_contact_edit_homepage(app):
    app.contact.check(Contact(homepage="facebook.com"))
    old_contacts = app.contact.get_contact_list()
    app.contact.edit_first_contact(Contact(homepage="new_facebook.com"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_contact_edit_bday(app):
    app.contact.check(Contact(bday="10"))
    old_contacts = app.contact.get_contact_list()
    app.contact.edit_first_contact(Contact(bday="1"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_contact_edit_bmonth(app):
    app.contact.check(Contact(bmonth="May"))
    old_contacts = app.contact.get_contact_list()
    app.contact.edit_first_contact(Contact(bmonth="June"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_contact_edit_byear(app):
    app.contact.check(Contact(byear="1959"))
    old_contacts = app.contact.get_contact_list()
    app.contact.edit_first_contact(Contact(byear="1999"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_contact_edit_aday(app):
    app.contact.check(Contact(aday="10"))
    old_contacts = app.contact.get_contact_list()
    app.contact.edit_first_contact(Contact(aday="1"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_contact_edit_amonth(app):
    app.contact.check(Contact(amonth="May"))
    old_contacts = app.contact.get_contact_list()
    app.contact.edit_first_contact(Contact(amonth="July"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_contact_edit_ayear(app):
    app.contact.check(Contact(ayear="2019"))
    old_contacts = app.contact.get_contact_list()
    app.contact.edit_first_contact(Contact(ayear="2029"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_contact_edit_address2(app):
    app.contact.check(Contact(address2="Something"))
    old_contacts = app.contact.get_contact_list()
    app.contact.edit_first_contact(Contact(address2="New Something"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_contact_edit_phone2(app):
    app.contact.check(Contact(phone2="070"))
    old_contacts = app.contact.get_contact_list()
    app.contact.edit_first_contact(Contact(phone2="080"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_contact_edit_notes(app):
    app.contact.check(Contact(notes="Best friend"))
    old_contacts = app.contact.get_contact_list()
    app.contact.edit_first_contact(Contact(notes="Best friend forever"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
