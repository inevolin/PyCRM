import os, json
from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/')
def index():
    return app.send_static_file('index.html')

def saveDataAtomic(data):
  f = open('data.tmp.json', 'w')
  f.write(data)
  f.flush()
  os.fsync(f.fileno()) 
  f.close()
  os.rename('data.tmp.json', 'data.json')

@app.route('/api/data', methods=['GET'])
def getData():
    with open('data.json') as json_file:
      return jsonify(json.load(json_file))

@app.route('/api/data', methods=['POST'])
def saveData():
    content = request.get_json()
    saveDataAtomic(json.dumps(content))
    return jsonify({'success':True})

## optional: disable file catching by browser
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
@app.after_request
def add_header(r):
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=1, port=7788)