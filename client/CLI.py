from FlaskApp import run_app
import pinggy
from threading import Thread
import time
import pyperclip

def start_flask():
    run_app()

def main():
    flask_thread = Thread(target=start_flask)
    flask_thread.start()
    time.sleep(2)
    
    tunnel = pinggy.start_tunnel(forwardto="127.0.0.1:5001")
    print(f"Server started. Link is available at {tunnel.urls[1]}")
    
    pyperclip.copy(tunnel.urls[1])
    print("Link copied to clipboard.")
    print("To close ChordAuth, close the terminal window or force quit it.")
    print("Thank you for using ChordAuth 🎹🔑😃")

if __name__ == "__main__":
    main()
