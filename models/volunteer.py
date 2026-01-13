"""Implements the Volunteer record class from Concat"""
from dataclasses import dataclass
from dataclasses_json import DataClassJsonMixin

from . import contact_method, department_assignment, user, option

#pylint: disable=C0103
@dataclass
class VolunteerRecord(DataClassJsonMixin):
    """The Volunteer record class from Concat"""

    createdAt: str
    updatedAt: str
    contactMethods: list[contact_method.ContactMethod]
    departments: list[department_assignment.DepartmentAssignment]
    user: user.User
    options: list[option.Option]
