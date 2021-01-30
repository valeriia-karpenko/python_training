# -*- coding: utf-8 -*-
import jsonpickle
import os.path
import random
import string
from model.contact import Contact
import getopt
import sys

try:
    opts, args= getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


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
               for i in range(n)
]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
