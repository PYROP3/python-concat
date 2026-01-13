"""Implements the Role classes from Concat"""
from dataclasses import dataclass
from dataclasses_json import DataClassJsonMixin

#pylint: disable=C0103
@dataclass
class Role(DataClassJsonMixin):
    """The Role class from Concat"""

    id: str
    name: str


@dataclass
class UserRole(Role):
    """The UserRole class from Concat"""

    scope: str
