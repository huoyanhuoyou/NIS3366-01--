from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import json
import psutil
import time
from selenium import webdriver
from urllib.parse import urlparse
from model import PasswordMemoModel,UserModel
from utils.password import create_pwd
from Global.GlobalConfig import GlobalConfig
from utils.Encryption import Encryption
def get_base_url(url):
    parsed_url = urlparse(url)
    base_url = f"{parsed_url.scheme}://{parsed_url.netloc}"
    return base_url
def checkurl(username, password, url):
    try:
        user = UserModel.get(UserModel.username == username, UserModel.password == password)
        password_memo = PasswordMemoModel.get(PasswordMemoModel.user == user,
                                                  PasswordMemoModel.url == url)
        return password_memo.account, password_memo.password, password_memo.key
    except:
        print("身份验证错误！")
        return None, None, None

app = Flask(__name__)

@app.route('/router', methods=['POST'])
@cross_origin()
def handle_ajax_request():
    data = request.get_json()

    print(data)

    username = data['username']
    password = data['password']
    weburl = data['url']
    # 在这里执行与数据库相关的操作
    password = create_pwd(username, password)
    url = get_base_url(weburl)

    user, pwd, key = checkurl(username, password, url)
    enc = Encryption()
    ret = enc.textDecrypt(pwd, private=GlobalConfig.file_path.private_key, key=key)
    pwd = ret.get('data')
    # 返回数据给
    response = {
        'message': '请求已成功处理',
        'data': {
            'account': user,
            'pwd':pwd
        }
    }
    return jsonify(response)
#测试方法
#curl http://localhost:5000/router -X POST -H "Content-Type: application/json" -d "{\"username\": \"33333\", \"password\": \"333333333\", \"url\": \"http://example.com\"}"
if __name__ == '__main__':
    app.run()