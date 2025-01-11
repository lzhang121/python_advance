# -*- coding: utf-8 -*-
# @Time : 2024/12/25 9:54
# @Author : zhanglei
# @Email : zhanglei@bonree.com
from flask import Flask, request, jsonify

app = Flask(__name__)


# 示例接口：获取请求信息
@app.route('/api/hello', methods=['GET'])
def hello_world():
	return jsonify({"message": "Hello, World!", "status": "success"})


# 示例接口：接收和处理POST请求
@app.route('/api/process', methods=['POST'])
def process_data():
	data = request.get_json()  # 获取POST请求中的JSON数据
	if not data:
		return jsonify({"error": "No data provided"}), 400

	# 模拟处理逻辑
	result = {"received_data": data, "message": "Data processed successfully!"}
	return jsonify(result)


# 示例接口：返回参数信息
@app.route('/api/echo', methods=['GET'])
def echo():
	param = request.args.get('param', 'default_value')  # 获取GET参数
	return jsonify({"param_received": param, "message": "This is an echo!"})


if __name__ == '__main__':
	# 启动应用程序
	app.run(debug=True, host='0.0.0.0', port=5500)