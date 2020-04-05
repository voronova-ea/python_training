from model.group import Group


def test_group_edit_all_fields(app):
    app.group.check(Group(name="name", header="header", footer="footer"))
    app.group.edit_first_group(Group(name="new name", header="new header", footer="new footer"))


def test_group_edit_all_fields_empty(app):
    app.group.check(Group(name="name", header="header", footer="footer"))
    app.group.edit_first_group(Group(name="", header="", footer=""))


def test_group_edit_name(app):
    app.group.check(Group(name="test"))
    app.group.edit_first_group(Group(name="new name"))


def test_group_edit_header(app):
    app.group.check(Group(header=""))
    app.group.edit_first_group(Group(header="new header"))


def test_group_edit_footer(app):
    app.group.check(Group(footer="test"))
    app.group.edit_first_group(Group(footer="new footer"))
