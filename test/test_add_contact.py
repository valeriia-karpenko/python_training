# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.open_contacts_page()
    app.contact.create(Contact(firstname="gfdgdfgdfg", middlename="sdfdfsdfsd", lastname="dfsdfsdf",
                               nickname="sdfdsfs", company="dfsdfds", address="fsdf"))
    app.session.logout()


def test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.open_contacts_page()
    app.contact.create(Contact(firstname="", middlename="", lastname="",
                               nickname="", company="", address=""))
    app.session.logout()
