"""
This is the people module and supports all the ReST actions for the
PEOPLE collection
"""
import json

from flask import Flask, jsonify, request

app = Flask(__name__)

customers = json.load(open('customers.json', 'r'))

# 3rd party modules
from flask import make_response, abort

# Data to serve with our API
customers = json.load(open('customers.json', 'r'))


def read_one(id_str):
    """
    This function responds to a request for /api/customers/{id}
    with one matching person from people

    :param id_str:
    :return:        person matching last name
    """
    # Does the person exist in people?
    filtered_customers = [c for c in customers if int(c['id']) == id_str]
    print(filtered_customers)

    if filtered_customers:
        pass
    # otherwise, nope, not found
    else:
        abort(
            404, "Person with last name {id_str} not found".format(lname=id_str)
        )

    return filtered_customers


def read_all():
    """
    This function responds to a request for /api/people
    with the complete lists of people

    :return:        json string of list of people
    """
    # Create the list of people from our data
    c = [c for c in customers]
    return c
