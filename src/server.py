from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs

hostName = "localhost"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):
    """
        Специальный класс, который отвечает за обработку
        входящих запросов от клиентов.
    """

    def do_GET(self):
        """ Метод для обработки входящих GET-запросов """
        if self.path == "/":
            page = "contacts.html"
        else:
            page = self.path[1:]
        try:
            with open(f"html_pages/{page}", "r", encoding="UTF-8") as page_html:
                self.send_response(200)
                self.send_header(keyword="Content-type", value="text/html")
                self.end_headers()
                self.wfile.write(page_html.read().encode("UTF-8"))
        except FileNotFoundError:
            self.send_error(404, "File Not Found")

    def do_POST(self):
        """ Метод для обработки POST-запросов """
        content_length = int(self.headers["Content-Length"])
        body = self.rfile.read(content_length).decode("UTF-8")

        parsed_data = parse_qs(body)
        decoded_data = {key: value for key, value in parsed_data.items()}

        print("Полученные данные:")
        for key, value in decoded_data.items():
            print(f"{key}: {value}")

        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write("Данные успешно получены!".encode("UTF-8"))


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))
    
    try: 
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass
    
    webServer.server_close()
    print("Server stopped.")
