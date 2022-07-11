from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.apzpx.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def home():
    return render_template('login.html')

# 로그인
@app.route("/api/login", methods=["POST"])
def web_mars_post():
    # name_give를 받아서 name_receive로 저장해라
    return jsonify({})

#회원가입
@app.route("/api/signup", methods=["POST"])
def web_mars_post():
    # name_give를 받아서 name_receive로 저장해라
    return jsonify({})

#글작성
@app.route("/api/posts", methods=["POST"])
def web_mars_post():
    # name_give를 받아서 name_receive로 저장해라
    return jsonify({})

#글목록
@app.route("//api/posts", methods=["GET"])
def web_mars_get():
    # db에서 조회할것을 가져와서 변수에 담는다.
    return jsonify({})

#검색
@app.route("/mars", methods=["GET"])
def web_mars_get():
    # db에서 조회할것을 가져와서 변수에 담는다.
    order_list = list(db.mars.find({},{'_id':False}))
    return jsonify({'orders': order_list})



if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)