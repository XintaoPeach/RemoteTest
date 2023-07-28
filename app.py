from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello():
    print('Hello Peach')
    return 'Hello Peach'


@app.route('/get_ip')
def ip():
    ip = request.remote_addr
    res = {
        '用户IP': ip
    }
    return res


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
