"""Implements the Option class from Concat"""
from typing import Tuple

from dataclasses import dataclass
from dataclasses_json import DataClassJsonMixin

#pylint: disable=C0103
@dataclass
class Option(DataClassJsonMixin):
    """The Option class from Concat"""

    name: str
    type: str
    value: Tuple[int, str, list[str]]
