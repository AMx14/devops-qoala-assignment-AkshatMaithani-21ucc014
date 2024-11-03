from flask import Flask, request
import datetime
import socket  # Note: This import is unused - can be removed
import netifaces as ni

app = Flask(__name__)

def get_mac_address():
    # Function to get the MAC address of the host
    for iface in ni.interfaces():
        try:
            # Added error handling for interfaces without MAC
            if ni.AF_LINK not in ni.ifaddresses(iface):
                continue
            mac = ni.ifaddresses(iface)[ni.AF_LINK][0]['addr']
            if mac:
                return mac
        except (KeyError, ValueError) as e:
            continue
    return "N/A"

@app.route('/')
def user_info():
    # Get user IP - using X-Forwarded-For header since we're behind Nginx
    user_ip = request.headers.get('X-Forwarded-For', request.remote_addr)

    # Get system username (from environment)
    username = request.headers.get('Username', 'Guest')

    # Get MAC address
    mac_address = get_mac_address()

    # Get current timestamp
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Added basic HTML structure and styling for better presentation
    return f"""
    <html>
    <head>
        <title>User Information</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 40px;
                line-height: 1.6;
            }}
            .container {{
                max-width: 600px;
                margin: 0 auto;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <p><b>IP Address:</b> {user_ip}</p>
            <p><b>MAC Address:</b> {mac_address}</p>
            <p><b>Username:</b> {username}</p>
            <p><b>Timestamp:</b> {timestamp}</p>
            <br>
            <h3>Assignment completed successfully!</h3>
        </div>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)