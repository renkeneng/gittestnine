# from flask import Flask
# app = Flask(__name__)

# #配置信息
# print(app.config)
# app.config['room'] = "105"
# app.config["MYSQL_HOST"] = "127.0.0.1"

# #获取配置信息
# print(app.config['room'])
# print(app.config["MYSQL_HOST"])

# @app.route('/')
# def hello_world():
#     return 'ET小仙女！'

# if __name__ == '__main__':
#     app.run(host="127.0.0.1",debug=True,port=8888)

# from flask import Flask
# # from settings import Config

# #定义一个配置类
# class Config:
#     ROOM = "105"
#     MYSQL_HOST = "127.0.0.1"

# app = Flask(__name__)

# app.config.from_object(Config)
# #配置信息
# print(app.config)
# print(app.config.get("ROOM"))
# print(app.config.get("MYSQL_HOST"))

# @app.route('/')
# def hello_world():
#     return 'ET小仙女'

# if __name__ == '__main__':
#     app.run(host="127.0.0.1",debug=True,port=8888)


# #导入Flask类库
# from flask import Flask
# #创建应用实例
# app = Flask(__name__)
# #视图函数（路由）
# @app.route('/')
# def index():
#     return '<h1>hello Flask!<h1>'
# #启动实施（只在当前模块运行）
# if __name__ == '__main__':
#     app.run()
    
# #导入flask类库
# from flask import Flask
# #创建应用实例
# app = Flask(__name__)
# #视图函数（路由）
# @app.route('/index')
# def index():
#     return '<h1>hello Flask!<h1>'
# #启动实施（只在当前模块运行）
# if __name__ == '__main__':
#     app.run()

# #导入flask类库
# from flask import Flask
# #创建应用实例
# app = Flask(__name__)
# #视图函数（路由）
# @app.route('/user/<username>')
# def say_hello(username):
#     return '<h1>Hello %s !<h1>' % username
# #启动实施（只在当前模块运行）
# if __name__ == '__main__':
#     app.run()

# #导入flask类库
# from flask import Flask
# #创建应用实例
# app = Flask(__name__)
# #视图函数（路由）
# @app.route('/user/<path:info>')
# def test(info):
#     return info
# #启动实施（只在当前模块运行）
# if __name__ == '__main__':
#     app.run()

#导入flask类库
# from contextlib import redirect_stderr
# from multiprocessing import managers
# from winreg import ExpandEnvironmentStrings
# from flask import Flask,request
# from sklearn.preprocessing import robust_scale
# #创建应用实例
# app = Flask(__name__)
# #request
# @app.route('/request/<path:info>')
# def request_url(info):
#     #完整的请求url
#     return request_url
#     '''
#     url:127.0.0.1:5000/request/abc/def?username=xiaoming&pwd=123
#     网页返回值：http://127.0.0.1:5000/request/abc/def?username=xiaoming&pwd=123
#     '''
#     #去掉GET参数的URL
#     return request.url
#     '''
#     网页返回值：http://127.0.0.1:5000/request/abc/def
#     '''
#     #只有主机和端口的url
#     return request.host_url
#     '''
#     网页返回值：http://127.0.0.1:5000/
#     '''
#     #装饰器中写的路由地址
#     return request.path
#     '''
#     网页返回值：/request/abc/def
#     '''
#     #请求方法类型
#     return request.method
#     '''
#     网页返回值：GET(也有可能是POST)
#     '''
#     #远程地址
#     return request.remote_addr
#     '''
#     网页返回值：127.0.0.1：5000
#     '''
#     #获取url参数
#     return request.args.get('username')
#     return request.args.get('pwd')
#     return str(request.args)
#     #获取headers信息
#     return request.headers.get('User-Agent')
# #启动实施（只在当前模块运行）
# if __name__ == '__main__':
#     app.run()

# from flask import Flask,make_response
# app = Flask(__name__)
# @app.route('/response')
# def response():
#     #不指定状态码，默认200，表示ok
#     #return 'OK'
#     #构造一个404状态码
#     #方法一
#     return 'not fount',404
#     #方法二
#     #导入make_response
#     #自定义构造一个响应，然后返回200，构造也可以指定状态码404
#     res = make_response('我是通过函数构造的响应',404)
#     return res
# if __name__ == '__main__':
#     app.run()


# from flask import Flask,redirect 
# app = Flask(__name__)
# @app.route('/old/')
# def old():
#     #return '这里是原始内容。’
#     #如果输入旧的old路由，会指向新的地址
#     #先输入一个外地请求试试
#     return redirect('https://www.baidu.com')
#     #再输入一个本地请求试试
#     return redirect('/new/')
#     #根据视图函数找到路由，指向方法：<url_for>中的参数'new’指向的是<函数名>
#     return redirect(url_for('new'))
#     return redirect(url_for('say_hello', username='xiaoming'))
# @app.route('/new/')
# def new():
#     return '这里是新的内容'
# if __name__ == '__main__':
#     app.run()

# from flask import Flask
# app = Flask(__name__)
# @app.route('/login/')
# def login():
#     #return '欢迎登陆’
#     #此处使用abort可以主动抛出异常
#     abort(404)
# if __name__ == '__main__':
#     app.run()

# from flask import Flask
# import time
# app = Flask(__name__)
# @app.route('/set_cookie/')
# def set_cookie():
#     resp = make_response('设置cookie')
#     #指定过期时间
#     expires = time.time + 10
#     resp.set_cookie('name','xiaoming',expires=expires)
#     return resp
# if __name__ == '__main__':
#     app.run()

# from flask import Flask, request
# app = Flask(__name__)
# @app.route('/get_cookie/')
# def get_cookie():
#     return request.cookie.get('name') or '你是哪个？'
# if __name__ == '__main__':
#     app.run()

# #发送到response的的headers里面（客户端）
# from flask import Flask,session
# import time,os
# '''
# 这里可以给secret_key设置一个随机n位字符串：os.urandom(n)
# '''
# app = Flask(__name__)
# #设置一个随机18位字符串的密钥，也可以设置成固定字符串
# app.config['SECRET_KEY'] = os.urandom(18)
# #app.config['SECRET_KEY'] = '这是个密钥字符串'
# @app.route('/set_session/')
# def set_session():
#     #session本身是个字典，需要直接添加键值对
#     '''
#     添加session值之前，必须先设置SECRET_KEY
#     '''
#     session['username'] = 'xiaoqiao'
#     return 'session已设置'
# @app.route('/get_session/')
# def get_session():
#     #获取session中的username的值，否则返回‘who are you?’
#     return session.get('username','who are you?')
# if __name__ == '__main__':
#     app.run()


# #命令行控制启动
# #导入类库
# from flask_script import Manager
# app = Flask(__name__)
# #创建对象
# manager = Manager(app)
# #启动程序
# if __name__ == '__main__':
#     #app.run()
#     #命令行控制启动
#     manager.run()

# from multiprocessing import managers
# from unicodedata import name
# from flask import Flask,render_template,render_template_string,g 
# from flask_script import Manger
# app = Flask(__name__)
# manager = Manger(app)
# @app.route('/index')
# def index():
#     #return'模版引擎测试'
#     #渲染模版文件
#     return render_template('index.html')
# @app.route('/index')
# def welcome(index):
#     #变量参数写在渲染函数的后面作为参数，前面的name是形参，后面的name是渲染模版中的解析内容
#     #return render_template('index.html',name=name)
#     #第二种方法，使用render_template_string(渲染字符串)
#     #return render_template_string('<h2>hello{{name}}!<h2>',name)
#     #第三种方法，使用g（全局函数），不需要分配就可以在模板中使用，
#     #只需要给定渲染模板即可；
#     g.name = name
#     return render_template('index.html')
# if __name__ == '__main__':
#     manager.run()

# from flask import Flask,render_template
# from flask_script import Manager
# app = Flask(__name__)
# manager = Manager(app)
# @app.route("rule")
# def use_func():
#     return render_template('use_func.html',var='hanmeimei')
#     return render_template('use_func.html',var='<b>xiaoming</b>')
# if __name__ == '__main__':
#     manager.run()


# from multiprocessing import managers
# from flask import Flask,render_template
# from flask_script import Manager
# app = Flask(__name__)
# manager = Manager(app)
# @app.route(/control/)
# def control():
#     #分配了该怎么处理，没有分配该怎么处理
#     return render_template('control.html',name='xiaoming')
# if __name__ == '__main__':
#     manager.run()

# from flask import Flask,render_template
# from flask_script import Manager
# app = Flask(__name__)
# manager = Manager(app)
# @app.route('/macro/')
# def macro():
#     return render_template('macro.html',name='xiaoming')
# if __name__ == '__main__':
#     manager.run()

# from flask import Flask, render_template
# from flask_script import Manager
# app = Flask(__name__)
# manager = Manager(app)
# @app.route('/include')
# def include():
#     return render_template('include.html',name='xiaoming')
# if __name__ == '__main__':
#     manager.run()

# from flask import Flask,render_template
# from flask_script import Manager
# app = Flask(__name__)
# manager = Manager(app)
# @app.route('/extends')
# def extends():
#     return render_template('children.html')
# if __name__ == '__main__':
#     manager.run()

# from ensurepip import bootstrap
# from flask_bootstrap import Bootstrap
# app = Flask(__name__)
# bootstrap = Bootstrap(app)
# @app.route('/bootstrap/')
# def bootstrap():
#     return render_template('bootstrap.html',name='xiaoming')
# if __name__ == '__main__':
#     manager.run()

# from flask_bootstrap import Bootstrap
# app = Flask(__name__)
# bootstrap= Bootstrap(app)
# @app.route('/')
# def base():
#     return render_template('base.html')
# if __name__ == '__main__':
#     manager.run()

#使用Flask创建服务器
#导入flask类
from urllib import response
from flask import Flask
from flask import request
from flask import jsonify
import json

#创建Flask实例，接收参数__name__表示当前文件名，默认会自动指定静态文件static
app = Flask(__name__)
#装饰器的作用是将路由器映射到视图函数get_age;告诉flask通过哪个URL可以出发函数
@app.route('/get_predict',methods=['POST'])
def get_age():
    input_json = request.json #调用服务器时输入的json字符串
    dict_json = json.loads(input_json)
    print(type(dict_json))
    x_1 = dict_json['height']
    x_2 = dict_json['weight']
    #此处可以加自己的特征处理，模型预测
    print(type(x_1))
    data = 0.5 * x_1 + 0.4 * x_2
    return str(data) #The return type must be a string, tuple #jsonify(data)
#Flask应用程序实例的run方法启动web服务器
if __name__ == '__main__':
    app.run(host='127.0.0.1',port=5000) #127.0.0.1 #指的是本地ip


    #使用requests访问服务器
    #调用API接口
    import requests
    import json

    base_url = 'http://127.0.0.1:5000/get_predict'
    data_json = json.dumps({'height':183,'weight':130}) #dumps:将python对象解码为json数据
    response = requests.post(base_url,json=data_json)
    predict_data = response.json()
    print('response:',response)
    print('response.text:',response.text)
    print('response.content:',response.content)
    print('predict_result',predict_data)

