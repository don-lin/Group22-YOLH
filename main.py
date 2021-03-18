from flask import Flask, send_from_directory, request
from crawler import lianjia_crawler

app = Flask(__name__, static_folder='static')


@app.route('/')
def hello_world():
    return send_from_directory('web', '主页.html')


@app.route('/map')
def send_map():
    return send_from_directory('web', '地址解析.html')


@app.route('/hot')
def send_hot_map():
    return send_from_directory('web', '热力地图.html')

@app.route('/hot2')
def send_hot2_map():
    return send_from_directory('web', '经纬度.html')

@app.route('/page/<path:temp>')
def send_static_file(temp):
    return send_from_directory("web", temp)


@app.route('/crawler/lianjia', methods=['POST', 'GET'])
def send_crawler_result():
    src = request.form.get('src')
    if not src is None:
        return str(lianjia_crawler.getCrawlerResult(src))
    return 'fail'


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=122)
