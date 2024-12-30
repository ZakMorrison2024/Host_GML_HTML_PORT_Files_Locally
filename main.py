import http.server
import socketserver
import os

# Configuration
PORT = 8080  # The port you want to serve on
DIRECTORY = "game_directory"  # Directory where your game files are stored

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        # Set the directory for the HTTP server
        super().__init__(*args, directory=DIRECTORY, **kwargs)

def main():
    # Change the working directory to the game's directory
    os.chdir(DIRECTORY)

    # Create a server object
    with socketserver.TCPServer(("", PORT), CustomHTTPRequestHandler) as httpd:
        print(f"Serving '{DIRECTORY}' at http://localhost:{PORT}")
        try:
            # Start the server
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")
            httpd.server_close()

if __name__ == "__main__":
    main()
