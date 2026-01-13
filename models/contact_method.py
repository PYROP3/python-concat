"""Implements the ContactMethod class from Concat"""
from dataclasses import dataclass
from dataclasses_json import DataClassJsonMixin

#pylint: disable=C0103
@dataclass
class ContactMethod(DataClassJsonMixin):
    """The ContactMethod class from Concat"""

    name: str
    isPrimary: bool
    value: str
