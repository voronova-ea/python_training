from model.group import Group


def test_group_edit(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(name="new name", header="new header", footer="new footer"))
    app.session.logout()


def test_group_edit_empty_fields(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(name="", header="", footer="1"))
    app.session.logout()