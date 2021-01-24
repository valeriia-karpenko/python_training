# -*- coding: utf-8 -*-
import random
import string

import pytest

from model.contact import Contact


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname="", lastname="", homephone="", email="", mobilephone="", workphone="", secondaryphone="",
                    address="", email2="", email3="")] + [
               Contact(firstname=random_string("firstname", 20), lastname=random_string("lastname", 10),
                       homephone=random_string("homephone", 10), email=random_string("email", 20),
                       mobilephone=random_string("mobilephone", 3), workphone=random_string("workphone", 2),
                       secondaryphone=random_string("secondaryphone", 2), address=random_string("address", 3),
                       email2=random_string("email2", 3), email3=random_string("email3", 2))
               for i in range(5)
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

# def test_add_contact(app):
#     old_contacts = app.contact.get_contact_list()
#     contact = Contact(firstname="Svetlana", lastname="Ivanova")
#     app.contact.create(contact)
#     assert len(old_contacts) + 1 == app.contact.count()
#     new_contacts = app.contact.get_contact_list()
#     old_contacts.append(contact)
#     assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


# def test_add_empty_contact(app):
#     old_contacts = app.contact.get_contact_list()
#     contact = Contact(firstname="", lastname="")
#     app.contact.create(contact)
#     assert len(old_contacts) + 1 == app.contact.count()
#     new_contacts = app.contact.get_contact_list()
#     old_contacts.append(contact)
#     assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
