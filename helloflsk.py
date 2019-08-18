from flask import Flask,render_template,request,redirect,url_for,abort,jsonify,make_response

app=Flask(__name__)
app.config['DEBUG']=True   #设置成调试模式程序出错Flask会返回500并会显示调试信息和错误堆栈

username='JGG'

@app.route('/index')
def index():
    return render_template('index.html',username=username)

@app.route('/hello/<name>')
def greet(name):
    return 'hello %s' %name  #动态视图函数

@app.route('/helloreq',methods=['GET','post'])   
def helloreq():
    return '<h1>hello,flask!<h1>'

@app.route('/helloredirect')
def helloredirect():
    return redirect(url_for('index'))    #内部视图函数跳转
    #return redirect('https://www.baidu.com')   #跳转到另外的地址

@app.route('/404')
def not_found():
    abort(404) 

@app.route('/foo')
def foo():
    
    return jsonify({'name':'Grey li','gender':'male'})
    #jsonify 会自动处理JSON生成JSON字符串

@app.route('/set/<name>')
def set_cookie(name):
    response=make_response(redirect(url_for('hello')))
    response.set










if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8090)