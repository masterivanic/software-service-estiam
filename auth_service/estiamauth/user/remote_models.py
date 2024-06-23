from django.conf import settings

class RemoteUserModel:

    def __init__(self, request, entity) -> None:
        self.request = request
        self.entity = entity
        self.url = f'{settings.ENTITY_BASE_URL_MAP.get(entity)}/api/{entity}'

    def _headers(self, override_headers=None):
        base_headers = {'content-type': 'application/json'}
        override_headers = override_headers or {}
        return {
            **self.request.META,
            **base_headers,
            **override_headers,
        }
    
    def _cookies(self, override_cookies=None):
        override_cookies = override_cookies or {}
        return {
        **self.request.COOKIES,
        **override_cookies,
    }