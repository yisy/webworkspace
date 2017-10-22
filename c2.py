#-*-coding=UTF-8 -*-

from flask import Flask,render_template,make_response,request,redirect,flash,get_flashed_messages

app = Flask(__name__)
app.jinja_env.line_statement_prefix='#'

app.secret_key = "133"


@app.route('/daf/')
def index():
    code = 1
    color=('red','blue')
    res = ''
    for msg in get_flashed_messages():
        res =  res + msg
    # return render_template('index.html',uid=code,color=color)
    return res

@app.route('/request')
def request_demo():
    # response = make_response('fdf00')
    # response.status = '404'
    # response.set_cookie('nowcoderid','fdssf')
    key = request.args.get('key','defaultkey')
    return key

@app.route('/re/<int:code>/')
def re(code):
    return redirect('/daf/',code=code)

@app.errorhandler(404)
def handler(error):
    return render_template('error.html',url=request.url)


@app.route('/login')
def login():
    flash('good')
    return 'okl'

if __name__ == '__main__':
    app.run(debug=True)  