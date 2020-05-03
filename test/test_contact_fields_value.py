from model.contact import Contact


def compare_contact_lists(app, chp, cdb):
    while len(chp) > 0:
        contact_from_home_page = chp.pop()
        contact_from_db = cdb.pop()
        assert contact_from_home_page.id == contact_from_db.id
        assert contact_from_home_page.firstname == app.contact.remove_end_or_begin_spaces(contact_from_db.firstname)
        assert contact_from_home_page.lastname == app.contact.remove_end_or_begin_spaces(contact_from_db.lastname)
        assert contact_from_home_page.address == app.contact.remove_end_or_begin_spaces(contact_from_db.address)
        assert contact_from_home_page.all_phones_from_home_page == app.contact.merge_phones_like_on_home_page(
            contact_from_db)
        assert contact_from_home_page.all_emails_from_home_page == app.contact.merge_emails_like_on_home_page(
            contact_from_db)


def test_contact_fields_value_on_home_page(app, db):
    app.contact.check(db, Contact(firstname="Homer", middlename="Jay", lastname="Simpson", nickname="Hommy",
                                  title="Some", company="NPS", address="Springfield", home="027220", mobile="567890",
                                  work="026789", fax="026790", email1="h.simpson@gmail.com",
                                  email2="h.simpson@somemail.com",
                                  email3="h.simpson@someelsemail.com", homepage="facebook.com", bday="10",
                                  bmonth="May",
                                  byear="1959", aday="10", amonth="May", ayear="2019", address2="Something",
                                  phone2="070",
                                  notes="Best friend"))

    contacts_from_home_page = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    contacts_from_db = sorted(db.get_contact_list(), key=Contact.id_or_max)
    compare_contact_lists(app, contacts_from_home_page, contacts_from_db)
