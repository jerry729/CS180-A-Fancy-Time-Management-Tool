import pytest
from django import forms
from django.core.exceptions import ValidationError
from myform import HelloForm

#to run: python -m pytest [test file name]

def test_valid_input():
    form_data = {
        'Username': 'BeanMan',
        'Password': '1234567'
    }
    form = HelloForm(data=form_data)
    assert form.is_valid() == True
    

def test_empty_username():
    form_data = {
        'Username': '',
        'Password': 'p@ssword'
    }
    form = HelloForm(data=form_data)
    assert form.is_valid() == False
    assert form.errors['Username'] == ['This field is required.']

def test_empty_password():
    form_data = {
        'Username': 'JohnDoe',
        'Password': ''
    }
    form = HelloForm(data=form_data)
    assert form.is_valid() == False
    assert form.errors['Password'] == ['This field is required.']