import random

from model.contact import Contact
from model.group import Group


def test_del_contact_to_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test"))
    # if len(db.get_groups_with_contacts()) == 0:
    if len(db.get_contacts_in_group()) == 0:
        groups = db.get_group_list()
        group = random.choice(groups)
        contacts = db.get_contacts_not_in_group()
        contact = random.choice(contacts)
        app.contact.add_contact_in_group(contact.id, group.id)
    groups = db.get_groups_with_contacts()
    group = random.choice(groups)
    old_contacts = db.get_contacts_in_group()
    contacts_from_group = db.get_contacts_in_group_by_group_id(group.id)
    contact = random.choice(contacts_from_group)
    app.contact.del_contact_from_group(contact.id, group.id)
    new_contacts = db.get_contacts_in_group()
    print(len(old_contacts))
    assert len(old_contacts) - 1 == len(new_contacts)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.group.get_group_list(), key=Contact.id_or_max)