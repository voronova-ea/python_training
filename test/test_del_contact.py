def test_delete_first_contact_from_main_page(app):
    app.contact.delete_first_contact_from_main_page()


def test_delete_first_contact_from_edit_form(app):
    app.contact.delete_first_contact_from_edit_form()
