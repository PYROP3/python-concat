"""Implements the Flag class from Concat"""
from dataclasses import dataclass
from dataclasses_json import DataClassJsonMixin

#pylint: disable=C0103
@dataclass
class Flag(DataClassJsonMixin):
    """The Flag class from Concat"""

    id: str
    shortName: str
