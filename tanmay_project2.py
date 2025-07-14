import http.server
import socket
import socketserver
import webbrowser
import pyqrcode
import os

# Set the port number
PORT = 8010

# Change directory to Desktop
desktop = os.path.join(os.path.expanduser("~"), "Desktop")
os.chdir(desktop)

# Create the HTTP request handler
Handler = http.server.SimpleHTTPRequestHandler

# Get local IP address
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try:
    s.connect(("8.8.8.8", 80))
    ip_address = s.getsockname()[0]
finally:
    s.close()

# Build the full link with port
link = f"http://{ip_address}:{PORT}"

# Generate QR code
url = pyqrcode.create(link)
url.svg("myqr.svg", scale=8)
url.png("myqr.png", scale=6)

# Open the SVG QR code in the browser
webbrowser.open("file://" + os.path.join(desktop, "myqr.svg"))

# Start the HTTP server
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at port {PORT}")
    print(f"Visit: {link}")
    print("Or scan the QR code")
    httpd.serve_forever()