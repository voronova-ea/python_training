from model.group import Group


def test_group_list(app, db):
    ui_list = app.group.get_group_list()

    def clean_spaces(group):
        return Group(id=group.id, name=group.name.strip() if group.name is not None else group.name)

    db_list = map(clean_spaces, db.get_group_list())
    assert sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)