from flask import Flask
import SQL 
import json
from flask import request
from flask import Flask, render_template
app = Flask(__name__)
#mpbill@gmail.com
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/test', methods=['POST'])
def test():
    print('anything')
    output = request.getjson()
    print(output)
    print(type(output))
    result = json.loads(output)
    print(result)
    print(type(result))
    SQL.connect()
    
test = request.getjson
if __name__=="__main__":
    app.run(debug=True)