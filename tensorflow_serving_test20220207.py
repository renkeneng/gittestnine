from cgi import MiniFieldStorage
from sklearn import metrics
import tensorflow as tf
#声明mnist对象，用于加载数据
mnist = tf.keras.datasets.mnist

#加载数据，并赋值给相关向量和数据声明
(x_train, y_train), (x_test, y_test) = mnist.load_data("mnist.npz")
print(x_train[0])
#将证书转为小数，也就是rgb小数
x_train, x_test = x_train/255.0, x_test/255.0

#创建模型，我们既可以通过new model,然后添加各层，也可以通过sequential定义各层，
model = tf.keras.models.Sequential([
    #将数据压缩为一维的，接受一个inputshape
    tf.keras.layers.Flatten(input_shape=(28,28)),
    #全连接层，将数据输出为128维的向量空间，激活函数为relu,可以有效梯度下降的激活函数
    tf.keras.layers.Dense(128,activation='relu'),
    #定义随机放弃的概率，用于减少计算量
    tf.keras.layers.Dropout(0.2),
    #全连接层，输出为10，激活函数为softmax分类函数。
    tf.keras.layers.Dense(10,activation='softmax')
])
model.compile(optimizer='adam',
loss='sparse_categorical_crossentropy',
metrics=['accuracy']
)
model.fit(x_train, y_train, epochs=5)
model.evaluate(x_test,y_test,verbose=2)
model.save("models/first",save_format='tf')

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