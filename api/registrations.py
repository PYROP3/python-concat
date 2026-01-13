"""Implements user-related API endpoints, such as getting a user by ID or searching for users."""

import typing

import requests

from models import registration

from . import concat

#pylint: disable=W3101

def get_registration(user_id: str) -> registration.Registration:
    r = requests.get(concat.BASE_URL + f'/api/v0/users/{user_id}/registration', headers={'Authorization': concat.ConcatServer.get_token()})

    if not r.ok:
        raise RuntimeError(f'Request failed: {r.content}')

    return registration.Registration.from_json(r.json)


# Documentation is fuzzy here, it says that userIds should be a number,
# but the example given shows an array of strings. For now we go with the example.
def search_registrations(next_page: str=None, limit: int=100, filter_user_ids: list[str]=None) -> typing.Tuple[list[registration.Registration], typing.Optional[str]]:
    data = {'limit': limit}

    if next_page:
        data['nextPage'] = next_page

    if filter_user_ids:
        data['filter'] = {'userIds': filter_user_ids}

    r = requests.post(concat.BASE_URL + '/api/v0/users/search', json=data, headers={'Authorization': concat.ConcatServer.get_token()})

    if not r.ok:
        raise RuntimeError(f'Request failed: {r.content}')

    registrations = [registration.Registration.from_json(u) for u in r.json.get('data', [])]

    return registrations, r.json.get('nextPage')


def _auto_search_registrations(limit: int=100, filter_user_ids: list[str]=None) -> list[registration.Registration]:
    registrations, next_page = search_registrations(limit=limit, filter_user_ids=filter_user_ids)

    while next_page is not None:
        more_registrations, next_page = search_registrations(next_page=next_page, limit=limit, filter_user_ids=filter_user_ids)
        registrations += more_registrations

    return registrations


def _lazy_search_registrations(limit: int=100, filter_user_ids: list[str]=None) -> typing.Generator[registration.Registration]:
    next_page = None

    while True:
        registrations, next_page = search_registrations(next_page=next_page, limit=limit, filter_user_ids=filter_user_ids)

        yield from registrations

        if next_page is None:
            break
