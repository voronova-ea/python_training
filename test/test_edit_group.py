from model.group import Group


def test_group_edit_all_fields(app):
    app.group.check(Group(name="name", header="header", footer="footer"))
    old_groups = app.group.get_group_list()
    group = Group(name="new name", header="new header", footer="new footer")
    group.id = old_groups[0].id
    app.group.edit_first_group(group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_group_edit_all_fields_empty(app):
    app.group.check(Group(name="name", header="header", footer="footer"))
    old_groups = app.group.get_group_list()
    app.group.edit_first_group(Group(name="", header="", footer=""))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_group_edit_name(app):
    app.group.check(Group(name="test"))
    old_groups = app.group.get_group_list()
    app.group.edit_first_group(Group(name="new name"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_group_edit_header(app):
    app.group.check(Group(header=""))
    old_groups = app.group.get_group_list()
    app.group.edit_first_group(Group(header="new header"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_group_edit_footer(app):
    app.group.check(Group(footer="test"))
    old_groups = app.group.get_group_list()
    app.group.edit_first_group(Group(footer="new footer"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
