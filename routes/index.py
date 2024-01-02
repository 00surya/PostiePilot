from flask import render_template

def home():
    return render_template('home.html')
def render_msg(msg):
    return render_template('msg.html', msg=msg)