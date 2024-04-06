from flask import Flask, request, jsonify
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
        return None, None, None

app = Flask(__name__)

@app.route('/router', methods=['POST'])
def handle_ajax_request():
    data = request.get_json()
    data = json.loads(data)
    username = data['username']
    password = data['password']
    weburl = data['weburl']
    # 在这里执行与数据库相关的操作
    password = create_pwd(username, password)
    url = get_base_url(weburl)

    user, pwd, key = checkurl(username, password, url)
    enc = Encryption()
    ret = enc.textDecrypt(pwd, private=GlobalConfig.file_path.private_key, key=key)
    pwd = ret.get('data')
    # 假设您要返回一些数据给JavaScript
    response = {
        'message': '请求已成功处理',
        'data': {
            'account': user,
            'pwd':pwd
        }
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run()