from printThread import PrintThread
from flask import Flask
app = Flask(__name__)

#
# flask paper display API.
#

# active thread
global thread
thread = None

# Default route
@app.route('/')
def index():
  return 'Server Works!'

# Change active display / refresh time
@app.route('/settings/<active>/<refreshTime>')
def settings(active, refreshTime):
  print_paper(active, refreshTime)
  return 'Settings updated... {}'.format(active)

def start_runner():
    print_paper('default', 120)

def print_paper(active, refreshTime):
    global thread
    if thread is not None:
        thread.stop()
        app.logger.info("Thread#Stopped")

    thread = PrintThread(active, refreshTime)
    thread.start()
    app.logger.info("Thread#Started")

# Start server
if __name__ == "__main__":
    start_runner()
    #app.run()
    app.run(host='0.0.0.0')
