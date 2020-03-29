def test_delete_first_contact_from_main_page(app):
    app.session.login(username="admin", password="secret")
    app.contact.delete_first_contact_from_main_page()
    app.session.logout()


def test_delete_first_contact_from_edit_form(app):
    app.session.login(username="admin", password="secret")
    app.contact.delete_first_contact_from_edit_form()
    app.session.logout()
