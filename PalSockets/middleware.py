from urllib.parse import parse_qs
from channels.db import database_sync_to_async

class SimpleAnonymousUser:
    is_authenticated = False

@database_sync_to_async
def get_user(user_id):
    return SimpleAnonymousUser()

class QueryAuthMiddleware:
    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
        query_string = scope.get("query_string", b"").decode("utf-8")
        query_params = parse_qs(query_string)
        user_id = query_params.get('user_id', [None])[0]

        if user_id and user_id.isdigit():
            scope['user'] = await get_user(int(user_id))
        else:
            scope['user'] = SimpleAnonymousUser()

        return await self.app(scope, receive, send)