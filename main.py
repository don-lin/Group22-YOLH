from flask import Flask, send_from_directory, request,jsonify,redirect
from crawler import lianjia_crawler
from ml import *

app = Flask(__name__, static_folder='static')


@app.route('/')
def hello_world():
    return send_from_directory('web', '主页.html')

@app.route('/buyers')
def send_buyers_page():
    return send_from_directory('web', 'buyers.html')

@app.route('/index')
def send_our_index():
    return redirect('/page/woodo/index.html')


@app.route('/map')
def send_map():
    return send_from_directory('web', '地址解析.html')


@app.route('/hot')
def send_hot_map():
    return send_from_directory('web', '热力地图.html')

@app.route('/hot2')
def send_hot2_map():
    return send_from_directory('web', '经纬度.html')

@app.route('/search')
def send_crawler_map():
    return send_from_directory('web', '搜索.html')
@app.route('/crawler')
def crawler():
    return send_from_directory('web', 'crawler.html')
@app.route('/page/<path:temp>')
def send_static_file(temp):
    return send_from_directory("web", temp)


@app.route('/crawler/lianjia', methods=['POST', 'GET'])
def send_crawler_result():
    src = request.form.get('src')
    if not src is None:
        return str(lianjia_crawler.getCrawlerResult(src))
    return 'fail'

@app.route('/query/date', methods=['POST', 'GET'])
def send_date_query_result():
    print('form is:',request.form)
    date = request.form.get('date')
    county=request.form.get('county')
    data=None
    if not date is None:
        data=getDF()
        data=queryDate(date,data)
        if not county is None and county!='Any County':
            data=queryCounty(county,data)
        data=convertDfList(data)
        return jsonify(data)
        return queryDate(date)
    return 'fail'

if __name__ == '__main__':
    app.run(debug=True,port=5000)
    #app.run(debug=True,host='0.0.0.0',port=122)

