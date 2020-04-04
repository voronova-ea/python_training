from model.group import Group


def test_group_edit_all_fields(app):
    app.group.edit_first_group(Group(name="new name", header="new header", footer="new footer"))


def test_group_edit_all_fields_empty(app):
    app.group.edit_first_group(Group(name="", header="", footer="1"))


def test_group_edit_name(app):
    app.group.edit_first_group(Group(name="new name"))


def test_group_edit_header(app):
    app.group.edit_first_group(Group(header="new header"))


def test_group_edit_footer(app):
    app.group.edit_first_group(Group(footer="new footer"))
