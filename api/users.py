"""Implements user-related API endpoints, such as getting a user by ID or searching for users."""

import typing

import requests

from models import user

from . import concat

#pylint: disable=W3101

def get_user(user_id: str) -> user.User:
    r = requests.get(concat.BASE_URL + f'/api/v0/users/{user_id}', headers={'Authorization': concat.ConcatServer.get_token()})

    if not r.ok:
        raise RuntimeError(f'Request failed: {r.content}')

    return user.User.from_json(r.json)


def search_users(next_page: str=None, limit: int=100, filter_role_id: int=None) -> typing.Tuple[list[user.User], typing.Optional[str]]:
    data = {'limit': limit}

    if next_page:
        data['nextPage'] = next_page

    if filter_role_id:
        data['filter'] = {'roleId': filter_role_id}

    r = requests.post(concat.BASE_URL + '/api/v0/users/search', json=data, headers={'Authorization': concat.ConcatServer.get_token()})

    if not r.ok:
        raise RuntimeError(f'Request failed: {r.content}')

    users = [user.User.from_json(u) for u in r.json.get('data', [])]

    return users, r.json.get('nextPage')


def _auto_search_users(limit: int=100, filter_role_id: int=None) -> list[user.User]:
    users, next_page = search_users(limit=limit, filter_role_id=filter_role_id)

    while next_page is not None:
        more_users = search_users(next_page=next_page, limit=limit, filter_role_id=filter_role_id)
        users += more_users

    return users


def _lazy_search_users(limit: int=100, filter_role_id: int=None) -> typing.Generator[user.User]:
    next_page = None

    while True:
        users, next_page = search_users(next_page=next_page, limit=limit, filter_role_id=filter_role_id)

        yield from users

        if next_page is None:
            break
