from printThread import PrintThread
from flask import Flask
app = Flask(__name__)

global thread
thread = None

def start_runner():
    print_paper('default')

@app.route('/')
def index():
  return 'Server Works!'

@app.route('/settings/<active>')
def settings(active):
  print_paper(active)
  return 'Settings updated... {}'.format(active)

def print_paper(active):
    global thread
    if thread is not None:
        thread.stop()
        app.logger.info("Thread#stopped")

    thread = PrintThread(active)
    thread.start()
    app.logger.info("Thread#started")

if __name__ == "__main__":
    start_runner()
    #app.run()
    app.run(host='0.0.0.0')
