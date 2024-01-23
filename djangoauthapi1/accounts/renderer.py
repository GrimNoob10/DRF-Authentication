from rest_framework import renderers
import json

class UserRenderer(renderers.JSONRenderer):
    charset = 'utf-8'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        if 'ErrorDetails' in str(data):
            response_data = {'error': data}
        else:
            response_data = data

        response = super().render(response_data, accepted_media_type, renderer_context)


        return response
