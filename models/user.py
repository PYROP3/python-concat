"""Implements the User class from Concat"""
from dataclasses import dataclass
from dataclasses_json import DataClassJsonMixin

from . import address

#pylint: disable=C0103
#pylint: disable=R0902
@dataclass
class User(DataClassJsonMixin):
    """The User class from Concat"""

    id: str
    email: str
    firstName: str
    lastName: str
    username: str
    verified: bool
    phone: str
    address: address.Address
    preferredName: str = None
