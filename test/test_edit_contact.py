from model.contact import Contact


def test_contact_edit_all_fields(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(firstname="New Homer", middlename="New Jay", lastname="New Simpson",
                                           nickname="New Hommy", title="New Some", company="New NPS",
                                           address="New Springfield", home="09", mobile="09", work="09",
                                           fax="09", email1="new_h.simpson@gmail.com",
                                           email2="new_h.simpson@somemail.com",
                                           email3="new_h.simpson@someelsemail.com", homepage="new_facebook.com",
                                           bday="1",
                                           bmonth="June", byear="1999", aday="1", amonth="June", ayear="2029",
                                           address2="New Something", phone2="007", notes="Best friend"))
    app.session.logout()


def test_contact_edit_all_fields_empty(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(firstname="", middlename="", lastname="", nickname="", title="", company="",
                                           address="", home="", mobile="", work="", fax="", email1="", email2="",
                                           email3="", homepage="", bday="-", bmonth="-", byear="", aday="-", amonth="-",
                                           ayear="", address2="", phone2="", notes=""))
    app.session.logout()


def test_contact_edit_firstname(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(firstname="New Homer"))
    app.session.logout()


def test_contact_edit_middlename(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(middlename="New Jay"))
    app.session.logout()


def test_contact_edit_lastname(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(lastname="New Simpson"))
    app.session.logout()


def test_contact_edit_nickname(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(nickname="New Hommy"))
    app.session.logout()


def test_contact_edit_title(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(title="New Some"))
    app.session.logout()


def test_contact_edit_company(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(company="New NPS"))
    app.session.logout()


def test_contact_edit_address(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(address="New Springfield"))
    app.session.logout()


def test_contact_edit_home(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(home="09"))
    app.session.logout()


def test_contact_edit_mobile(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(mobile="09"))
    app.session.logout()


def test_contact_edit_work(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(work="09"))
    app.session.logout()


def test_contact_edit_fax(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(fax="09"))
    app.session.logout()


def test_contact_edit_email1(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(email1="new_h.simpson@gmail.com"))
    app.session.logout()


def test_contact_edit_email2(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(email2="new_h.simpson@somemail.com"))
    app.session.logout()


def test_contact_edit_email3(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(email3="new_h.simpson@someelsemail.com"))
    app.session.logout()


def test_contact_edit_homepage(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(homepage="new_facebook.com"))
    app.session.logout()


def test_contact_edit_bday(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(bday="1"))
    app.session.logout()


def test_contact_edit_bmonth(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(bmonth="June"))
    app.session.logout()


def test_contact_edit_byear(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(byear="1999"))
    app.session.logout()


def test_contact_edit_aday(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(aday="1"))
    app.session.logout()


def test_contact_edit_amonth(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(amonth="July"))
    app.session.logout()


def test_contact_edit_ayear(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(ayear="2029"))
    app.session.logout()


def test_contact_edit_address2(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(address2="New Something"))
    app.session.logout()


def test_contact_edit_phone2(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(phone2="007"))
    app.session.logout()


def test_contact_edit_notes(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(notes="Best friend"))
    app.session.logout()