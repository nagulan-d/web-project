from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return ' Webhook server is running.'

@app.route('/webhook', methods=['POST'])
def webhook():
    subprocess.call(['./deploy.sh'])
    return ' Webhook received and deployment triggered.', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
