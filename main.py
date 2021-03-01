from flask import Flask,send_from_directory


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/map')
def send_map():
    return send_from_directory('.','地址解析.html')

if __name__ == '__main__':
    app.run(debug=True)


