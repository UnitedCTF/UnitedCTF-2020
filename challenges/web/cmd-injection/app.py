import os
import sys

from flask import Flask, render_template, request

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True      
app.jinja_env.auto_reload = True

@app.route("/", methods=["GET"])
def get_index():
    return render_template("index.html")

@app.route("/", methods=["POST"])
def post_index():
    text = request.form.get("text")
    cmd = f"echo '{text}' | grep -oiP 'FLAG-[abcdef0-9]+'"

    print(cmd)
    stream = os.popen(cmd)
    
    return render_template("index.html", output = stream.read())

@app.route("/source")
def source():
    with open(__file__, "r") as f:
        code = f.read()
    
    return render_template("code.html", code = code)
