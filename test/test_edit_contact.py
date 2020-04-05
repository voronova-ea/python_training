from model.contact import Contact


def test_contact_edit_all_fields(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="", middlename="", lastname="", nickname="", title="", company="",
                               address="", home="", mobile="", work="", fax="", email1="", email2="", email3="",
                               homepage="", bday="", bmonth="-", byear="", aday="", amonth="-", ayear="", address2="",
                               phone2="", notes=""))
    app.contact.edit_first_contact(Contact(firstname="New Homer", middlename="New Jay", lastname="New Simpson",
                                           nickname="New Hommy", title="New Some", company="New NPS",
                                           address="New Springfield", home="09", mobile="09", work="09",
                                           fax="09", email1="new_h.simpson@gmail.com",
                                           email2="new_h.simpson@somemail.com",
                                           email3="new_h.simpson@someelsemail.com", homepage="new_facebook.com",
                                           bday="1", bmonth="June", byear="1999", aday="1", amonth="June", ayear="2029",
                                           address2="New Something", phone2="007", notes="Best friend"))


def test_contact_edit_all_fields_empty(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Homer", middlename="Jay", lastname="Simpson", nickname="Hommy",
                               title="Some", company="NPS", address="Springfield", home="027220", mobile="567890",
                               work="026789", fax="026790", email1="h.simpson@gmail.com", email2="h.simpson@somemail.com",
                               email3="h.simpson@someelsemail.com", homepage="facebook.com", bday="10", bmonth="May",
                               byear="1959", aday="10", amonth="May", ayear="2019", address2="Something", phone2="007",
                               notes="Best friend"))
    app.contact.edit_first_contact(Contact(firstname="", middlename="", lastname="", nickname="", title="", company="",
                                           address="", home="", mobile="", work="", fax="", email1="", email2="",
                                           email3="", homepage="", bday="-", bmonth="-", byear="", aday="-", amonth="-",
                                           ayear="", address2="", phone2="", notes=""))


def test_contact_edit_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Homer"))
    app.contact.edit_first_contact(Contact(firstname="New Homer"))


def test_contact_edit_middlename(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(middlename="Jay"))
    app.contact.edit_first_contact(Contact(middlename="New Jay"))


def test_contact_edit_lastname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(lastname=""))
    app.contact.edit_first_contact(Contact(lastname="New Simpson"))


def test_contact_edit_nickname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(nickname="Hommy"))
    app.contact.edit_first_contact(Contact(nickname="New Hommy"))


def test_contact_edit_title(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(title=""))
    app.contact.edit_first_contact(Contact(title="New Some"))


def test_contact_edit_company(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(company="NPS"))
    app.contact.edit_first_contact(Contact(company="New NPS"))


def test_contact_edit_address(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(address="Springfield"))
    app.contact.edit_first_contact(Contact(address="New Springfield"))


def test_contact_edit_home(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(home=""))
    app.contact.edit_first_contact(Contact(home="09"))


def test_contact_edit_mobile(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(mobile="567890"))
    app.contact.edit_first_contact(Contact(mobile="09"))


def test_contact_edit_work(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(work="026789"))
    app.contact.edit_first_contact(Contact(work="09"))


def test_contact_edit_fax(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(fax=""))
    app.contact.edit_first_contact(Contact(fax="09"))


def test_contact_edit_email1(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(email1="h.simpson@gmail.com"))
    app.contact.edit_first_contact(Contact(email1="new_h.simpson@gmail.com"))


def test_contact_edit_email2(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(email2="h.simpson@somemail.com"))
    app.contact.edit_first_contact(Contact(email2="new_h.simpson@somemail.com"))


def test_contact_edit_email3(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(email3="h.simpson@someelsemail.com"))
    app.contact.edit_first_contact(Contact(email3="new_h.simpson@someelsemail.com"))


def test_contact_edit_homepage(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(homepage="facebook.com"))
    app.contact.edit_first_contact(Contact(homepage="new_facebook.com"))


def test_contact_edit_bday(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(bday="10"))
    app.contact.edit_first_contact(Contact(bday="1"))


def test_contact_edit_bmonth(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(bmonth="May"))
    app.contact.edit_first_contact(Contact(bmonth="June"))


def test_contact_edit_byear(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(byear="1959"))
    app.contact.edit_first_contact(Contact(byear="1999"))


def test_contact_edit_aday(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(aday="10"))
    app.contact.edit_first_contact(Contact(aday="1"))


def test_contact_edit_amonth(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(amonth="May"))
    app.contact.edit_first_contact(Contact(amonth="July"))


def test_contact_edit_ayear(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(ayear="2019"))
    app.contact.edit_first_contact(Contact(ayear="2029"))


def test_contact_edit_address2(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(address2="Something"))
    app.contact.edit_first_contact(Contact(address2="New Something"))


def test_contact_edit_phone2(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(phone2="007"))
    app.contact.edit_first_contact(Contact(phone2="008"))


def test_contact_edit_notes(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(notes="Best friend"))
    app.contact.edit_first_contact(Contact(notes="Best friend forever"))