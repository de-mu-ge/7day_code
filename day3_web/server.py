import json
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

stu = []
try:
    f = open('students.json', 'r', encoding='utf-8')
    stu = json.load(f)
    f.close()
except Exception:
    pass


def save():
    f = open('students.json', 'w', encoding='utf-8')
    json.dump(stu, f, ensure_ascii=False, indent=2)
    f.close()


def send_json(self, data):
    self.send_response(200)
    self.send_header('Content-Type', 'application/json; charset=utf-8')
    self.end_headers()
    self.wfile.write(json.dumps(data, ensure_ascii=False).encode('utf-8'))


class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        url = urlparse(self.path)
        if url.path.startswith('/api'):
            send_json(self, stu)
            return
        path = 'static/index.html' if url.path == '/' else 'static' + url.path
        try:
            f = open(path, 'rb')
            data = f.read()
            f.close()
            self.send_response(200)
            if path.endswith('.css'):
                self.send_header('Content-Type', 'text/css')
            elif path.endswith('.js'):
                self.send_header('Content-Type', 'application/javascript')
            else:
                self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(data)
        except Exception:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(length).decode('utf-8')
        s = json.loads(body)
        s['id'] = len(stu) + 1
        stu.append(s)
        save()
        send_json(self, {'ok': True})

    def do_PUT(self):
        length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(length).decode('utf-8')
        s = json.loads(body)
        for x in stu:
            if x['id'] == s['id']:
                x['name'] = s['name']
                x['age'] = s['age']
                x['score'] = s['score']
        save()
        send_json(self, {'ok': True})

    def do_DELETE(self):
        query = parse_qs(urlparse(self.path).query)
        sid = int(query.get('id', [0])[0])
        for x in stu:
            if x['id'] == sid:
                stu.remove(x)
        save()
        send_json(self, {'ok': True})


print('服务已启动，打开浏览器访问 http://127.0.0.1:8000')
HTTPServer(('127.0.0.1', 8000), Handler).serve_forever()
