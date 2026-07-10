import http.server
import os

PORT = 3000
DIR = os.path.dirname(os.path.abspath(__file__))


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIR, **kwargs)

    def do_GET(self):
        # 根路径重定向到 N7O.html
        path = self.path.split('?')[0].split('#')[0]
        if path == '/':
            self.path = '/N7O.html'
        super().do_GET()


if __name__ == '__main__':
    print(f'服务器已启动: http://localhost:{PORT}')
    http.server.HTTPServer(('', PORT), Handler).serve_forever()