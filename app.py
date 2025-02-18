from flask import Flask
import os
import subprocess
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/htop')
def htop():
    name = "Deep Radadiya"
    username = os.getenv("USER") or os.getenv("USERNAME") or "Unknown User"
    
    # Get current time in IST
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S IST')

    # Fetch system processes using 'top' command
    try:
        top_output = subprocess.getoutput("top -b -n 1 | head -10")
    except Exception as e:
        top_output = f"Error fetching system info: {e}"

    return f"""
    <h1>System Details</h1>
    <p><b>Name:</b> {name}</p>
    <p><b>Username:</b> {username}</p>
    <p><b>Server Time (IST):</b> {server_time}</p>
    <pre>{top_output}</pre>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
