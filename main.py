from flask import Flask,send_from_directory


app = Flask(__name__,static_folder='static')

@app.route('/')
def hello_world():
    return send_from_directory('.','主页.html')

@app.route('/map')
def send_map():
    return send_from_directory('.','地址解析.html')

@app.route('/hotmap')
def hot_map():
    return send_from_directory('.','热力地图.html')

@app.route('/page/<path:temp>')
def send_static_file(temp):
    print('hello!')
    return send_from_directory("web",temp)

if __name__ == '__main__':
    app.run(debug=True)


