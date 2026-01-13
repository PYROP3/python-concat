"""Implements the Address class from Concat"""
from dataclasses import dataclass
from dataclasses_json import DataClassJsonMixin

#pylint: disable=C0103
@dataclass
class Address(DataClassJsonMixin):
    """The Address class from Concat"""

    addressCity: str
    addressCountry: str
    addressLine1: str
    addressState: str
    addressZipcodoe: str
    addressLine2: str = None
