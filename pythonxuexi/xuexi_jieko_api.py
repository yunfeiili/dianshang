import hashlib,time

from flask import Flask, request, jsonify
import json,jwt
import datetime


app = Flask(__name__)

# 密钥用于签名 JWT Token
SECRET_KEY = "your_secret_key"

# 模拟数据库存储用户数据

users_db = {
'andmi': {'password': 12213123456}
}


def read_users_data():
    try:
        with open("../data/users.json",mode="r",encoding="utf-8") as file:
            value = json.load(file)
            return value
    except:
        value = {}
        return value


def write_users_data(datas):
    # 读取现有数据
    # try:
    #     with open("../data/users.json", "r", encoding="utf-8") as file:
    #         data = json.load(file)  # 返回字典
    # except FileNotFoundError:
    #     data = {}  # 文件不存在时初始化空字典
    data = read_users_data()
    # 合并数据（更新旧字段，添加新字段）
    data.update(datas)

    # 重新写入文件
    with open("../data/users.json", "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)



users_dbs = read_users_data()

@app.route('/register', methods=['POST'])
def register():
    """
    注册新用户。
    输入：用户名 (username)，密码 (password)
    输出：成功消息或错误提示
    """
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"error": "Username and Password are required.",
                          "success":False
                       }), 400
    users_dbs = read_users_data()
    if username in users_dbs:
        return jsonify({"error": "User already exists.用户已存在。",
                          "success":False
                       }), 409

    users = {
        username:{"password":password}
        }
    write_users_data(users)
    return jsonify({"message": "User registered successfully.恭喜注册成功",
                          "success":True
                   }), 201



@app.route('/login', methods=['POST'])
def login():
    """
    用户登录并生成 Token。
    输入：用户名 (username)，密码 (password)
    输出：Token 或错误提示
    """
    data = request.json
    username = data.get('username')
    password = data.get('password')

    user = users_dbs.get(username)

    if not user or user["password"] != password:
        return jsonify({"error": "Invalid credentials.账号密码不正确",
                          "success":False
                       }), 401

    # 创建 Token
    token_payload = {
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1),
        'iat': datetime.datetime.utcnow(),
        'sub': username
    }
    token = jwt.encode(token_payload, SECRET_KEY, algorithm='HS256')  # 使用 HS256 算法加密
    return jsonify({'token': token,
                    "username": username,
                    "msg":f"恭喜用户 {username} 登录成功",
                    "success": True
                    }
                   ), 200


@app.route('/query', methods=['GET'])
def query():
    """
    查询接口，需携带有效的 Token。
    输入：无
    输出：欢迎信息或错误提示
    """
    auth_header = request.headers.get('Authorization')

    if not auth_header:
        return jsonify({"error": "Missing Authorization header."}), 401

    try:
        token = auth_header
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])  # 验证 Token
        username = payload['sub']
        # traceId = str(time.time())
        return jsonify({"message": f"Welcome, {username}!",
                    "traceId": hashlib.md5(str(time.time()).encode()).hexdigest(),
                    "success":True
                        })
    except jwt.ExpiredSignatureError:
        return jsonify({"error": "Token has expired.",
                          "success":False
                       }), 401
    except jwt.InvalidTokenError:
        return jsonify({"error": "Invalid Token.",
                          "success":False
                       }), 401



@app.route('/delete/<string:username>', methods=['DELETE'])
def delete_user(username):
    """
    删除指定用户。
    输入：用户名 (路径参数)
    输出：删除成功的消息或错误提示
    """
    if username not in users_db:
        return jsonify({"error": "User does not exist.",
                          "success":False
                       }), 404

    del users_db[username]
    return jsonify({"message": "User deleted successfully.",
                    "success":True
                   }), 200


if __name__ == '__main__':
    app.run(debug=True,port = 8801)
