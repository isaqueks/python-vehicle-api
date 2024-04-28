# Python 3 server example
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import env
import json

hostName = "localhost"
serverPort = env.PORT

from providers.tabelafipe_pro_br import TabelaFipeProBrProvider

provider = TabelaFipeProBrProvider()

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):

        try:
            plate = self.path.split("/")[1].upper()
            if plate == "":
                self.send_response(400)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                self.wfile.write(bytes(json.dumps({"error": "Invalid plate"}), "utf-8"))
                return

            veh = provider.fetch_vehicle(plate).__dict__

            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(bytes(json.dumps(veh), "utf-8"))
        except Exception as ex:
            print(ex)
            self.send_response(500)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(bytes(json.dumps({"error": "Internal Server Error"}), "utf-8"))

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")