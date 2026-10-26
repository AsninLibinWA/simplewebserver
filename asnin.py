from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<html>
    <head>
      <title>My Pc</title>
      </head>
      <h2>
      Asnin Libin 26004114
      </h2>
    
      <table border="1" cellspacing="10" cellpadding="10"
      <tr bgcolor="">
        <th>S.No</th>
        <th>DEVICE NAME</th>
        <th>PROCESSOR</th>
        <th>INSTALLED RAM</th>
        <th>GRAPHICS CARD</th>
        <th>STORAGE</th>)
        </tr>
      <tr>
          <td>1</td>
          <td>TL15-53M-G2</td>
          <td>Intel(R) Core(TM) 5 210H (2.20GHz)</td>
          <td>16.0 GB (15.7 GB usable)</td>
          <td>Intel(R) Graphics (128 MB)</td>
          <td>126 GB of 477 GB used</td>
          </tr>
          </table>
      </body> 
        
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Client request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my own webserver is running successfully...")
httpd.serve_forever()