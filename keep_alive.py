# To Keep the Bot Alive 24/7

# Host the Bot at Replit to Work More Efficiently Using This 

from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def main():
    done = "I'm Alive"
    return f"{done}"
    

def run():
    app.run(host="0.0.0.0", port=8080)

def keep_alive():
    server = Thread(target=run)
    server.start()
