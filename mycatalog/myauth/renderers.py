import json

from rest_framework.renderers import JSONRenderer

class UserRenderer(JSONRenderer):

    charset = "utf-8"

    def render(self, data, media_type=None, renderer_context=None):

        # Handle the non-text token key in the response, if there is one
        token = data.get("token", None)
        if token is not None and isinstance(token, bytes):
            data["token"] = token.decode("utf-8")

        return json.dumps({
            "user": data
        })