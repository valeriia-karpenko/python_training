# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modify_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Svetlana", lastname="Ivanova"))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_contact(Contact(firstname="gyt", middlename="frewrwe", lastname="utyut"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)



def test_modify_empty_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Svetlana", lastname="Ivanova"))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_contact(Contact(firstname="", middlename="", lastname=""))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
