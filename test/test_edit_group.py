from model.group import Group


def test_group_edit_all_fields(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(name="new name", header="new header", footer="new footer"))
    app.session.logout()


def test_group_edit_all_fields_empty(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(name="", header="", footer="1"))
    app.session.logout()


def test_group_edit_name(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(name="new name"))
    app.session.logout()


def test_group_edit_header(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(header="new header"))
    app.session.logout()


def test_group_edit_footer(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(footer="new footer"))
    app.session.logout()
