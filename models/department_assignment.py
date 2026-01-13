"""Implements the DepartmentAssignment class from Concat"""
from dataclasses import dataclass
from dataclasses_json import DataClassJsonMixin

#pylint: disable=C0103
@dataclass
class DepartmentAssignment(DataClassJsonMixin):
    """The DepartmentAssignment class from Concat"""

    id: str
    states: list[str]
    name: str
