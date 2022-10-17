from http.server import BaseHTTPRequestHandler
from models import Property
from urllib.parse import urlparse, parse_qs

import json


class Handler(BaseHTTPRequestHandler):

    def _get_params(self):
        dict_params = parse_qs(urlparse(self.path).query)
        print("_get_params", dict_params)
        return dict_params

    def _set_headers_service(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_GET(self):
        self._set_headers_service()
        property = Property()
        dict_data = property.get_property_by_state(self._get_params())
        json_data = json.dumps(dict_data)
        self.wfile.write(json_data.encode('utf-8'))
