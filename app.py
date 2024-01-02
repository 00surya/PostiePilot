from flask import Flask, request
from routes import index
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hello123'

app.add_url_rule('/', view_func=index.home, methods=['GET'])
app.add_url_rule('/<string:msg>', view_func=index.render_msg, methods=['GET'])

if __name__=='__main__':
    app.run(debug=True)