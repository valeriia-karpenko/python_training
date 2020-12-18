# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application
from model.contact import Contact


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.open_contacts_page()
    app.create_contact(Contact(firstname="gfdgdfgdfg", middlename="sdfdfsdfsd", lastname="dfsdfsdf",
                               nickname="sdfdsfs", company="dfsdfds", address="fsdf"))
    app.session.logout()


def test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.open_contacts_page()
    app.create_contact(Contact(firstname="", middlename="", lastname="",
                               nickname="", company="", address=""))
    app.session.logout()
