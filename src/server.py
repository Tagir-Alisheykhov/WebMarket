from http.server import BaseHTTPRequestHandler, HTTPServer

hostName = "local_host"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):
    """
        Специальный класс, который отвечает за обработку
        входящих запросов от клиентов.
    """

    def do_GET(self):
        """ Метод для обработки входящих GET-запросов """
        self.send_response(200)
        self.send_header(keyword="Content-type", value="application/json")
        self.end_headers()
        self.wfile.write(bytes("{'message': 'OK'}", "UTF-8"))

    def do_POST(self):
        """ Метод для обработки POST-запросов """
        content_length = int(self.headers["Content-Length"])
        body = self.rfile.read(content_length)
        print(body)
        self.send_response(200)
        self.end_headers()


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
