from flask import Flask,send_from_directory


app = Flask(__name__,static_folder='static')

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/map')
def send_map():
    return send_from_directory('.','地址解析.html')

@app.route('/page/<path:temp>')
def send_static_file(temp):
    print('hello!')
    return send_from_directory("web",temp)

if __name__ == '__main__':
    app.run(debug=True)


