from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['Debug']=True

form = """
<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
           }}
        </style>
    </head>
    <body>
     <form>
        <label> Rotate by: 
        <input type="text" name="rot" value=0/> 
        </label> <br/>
        <textarea name="text">{0}</textarea> 
        <br/>
        <button type="submit" value="submit">Submit Query</button>
    </form>
    </body>
</html>
"""
@app.route("/")
def index():
     return form.format("")

@app.route("/", methods=['POST'])
def encrypt():
    text = request.form['text']
    rot =int(request.form['rot'])
    answer = rotate_string(text,rot)
    return form.format(answer)

app.run()


