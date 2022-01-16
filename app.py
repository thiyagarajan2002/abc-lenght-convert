from logging import exception
from flask import Flask, render_template,url_for,request
import convert
import Database

app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def Home():
    return render_template('home.html')

@app.route("/result", methods=['POST','GET'])
def result():
  try:
    from_value1 = (request.form['from'])
    to_value1 = (request.form['to'])
    size1 = (request.form['value'])
    ls=['mm','cm','m','km','in','ft','yd','mi']
    from_value2=ls.index(from_value1)
    to_value2=ls.index(to_value1)
    result1=convert.convert(int(from_value2),int(to_value2),float(size1))
    result1=str(result1)
    Database.write(from_value1,to_value1,size1,result1)
    return render_template('home.html', result2=result1)
  except:
    return render_template('home.html', result2='Invalid Input')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)

    
