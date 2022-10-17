from http.server import HTTPServer
from http_handler import Handler

if __name__ == '__main__':
    webServer = HTTPServer(('localhost', 8080), Handler)
    print("Server started http://%s:%s" % ('localhost', 8080))
    webServer.serve_forever()
