import datetime
# import enum
import os
import requests

from dataclasses import dataclass


BASE_URL = os.getenv('CONCAT_BASE_URL')
if BASE_URL is None:
    raise RuntimeError('Missing CONCAT_BASE_URL environment variable')

BASE_URL = BASE_URL.rstrip('/')

CLIENT_ID = os.getenv('CONCAT_OAUTH_CLIENT_ID')
CLIENT_SECRET = os.getenv('CONCAT_OAUTH_CLIENT_SECRET')

if CLIENT_ID is None:
    raise RuntimeError('Missing CONCAT_OAUTH_CLIENT_ID environment variable')
if CLIENT_SECRET is None:
    raise RuntimeError('Missing CONCAT_OAUTH_CLIENT_SECRET environment variable')

# class ServiceIntegrationScope(enum.Enum):
#     USER_READ = 'user:read'
#     USER_ROLES_UPDATE = 'user:roles:update'
#     REGISTRATION_READ = 'registration:read'
#     VOLUNTEER_READ = 'volunteer:read'

OAUTH_SCOPE = os.getenv('CONCAT_OAUTH_SCOPE', 'user:read registration:read volunteer:read')


@dataclass
class ServiceToken:
    access_token: str
    expires_at: datetime.datetime
    scope: str
    # scopes: list[ServiceIntegrationScope]

    def is_valid(self):
        return datetime.datetime.now() >= self.expires_at


class ConcatServer:
    bearer_token: ServiceToken

    @staticmethod
    def get_token():
        if ConcatServer.bearer_token.is_valid():
            return ConcatServer.bearer_token

#         curl https://reg.mybigevent.org \
#   -X POST \
#   -H "Content-Type: application/x-www-form-urlencoded" \
#   -d "client_id=123" \
#   -d "client_secret=abc" \
#   -d "grant_type=client_credentials" \
#   -d "scope=user%3Aread"

        data = {
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
            'grant_type': 'client_credentials',
            'scope': OAUTH_SCOPE
        }

        r = requests.post(BASE_URL + '/api/oauth/token', data=data)

        if not r.ok:
            raise RuntimeError(f'Failed to obtain oauth token: {r.content}')

        resp = r.json()

#         {
#   "access_token": "...",
#   "expires_in": 3600,
#   "scope": "user:read",
#   "token_type": "Bearer",
# }

        access_token = resp['access_token']
        expires_at = datetime.datetime.now() + datetime.timedelta(seconds=resp['expires_in'])
        scope = resp['scope']

        ConcatServer.bearer_token = ServiceToken(access_token, expires_at, scope)

ConcatServer.get_token()
