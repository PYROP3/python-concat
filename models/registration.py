"""Implements the Registration class from Concat"""
from dataclasses import dataclass
from dataclasses_json import DataClassJsonMixin

from . import option, flag, user

#pylint: disable=C0103
#pylint: disable=R0902
@dataclass
class Registration(DataClassJsonMixin):
    """The Registration class from Concat"""

    createdAt: str
    updatedAt: str
    badgeName: str
    status: str
    productName: str
    productDisplayName: str
    productId: str
    options: list[option.Option]
    flags: list[flag.Flag]
    user: user.User
