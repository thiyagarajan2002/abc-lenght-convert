from logging import exception
from flask import Flask, render_template,url_for,request

# Start code

#Millimeter
def convert(from_value,to_value,size):
    #Millimeter
    if from_value==0:
        if to_value==0:
            res=size
            
        elif to_value==1:
            res=size/10
            
        elif to_value==2:
            res=size/1000
            
        elif to_value==3:
            res=size/1000000
            
        elif to_value==4:
            res=size/25.4
            
        elif to_value==5:
            res=size/305
            
        elif to_value==6:
            res=size/914
            
        elif to_value==7:
            res=size*39.37
            
    #Centimeter
    elif from_value==1:
        if to_value==0:
            res=size/10
            
        elif to_value==1:
            res=size
            
        elif to_value==2:
            res=size/100
            
        elif to_value==3:
            res=size/100000
            
        elif to_value==4:
            res=size/2.54
            
        elif to_value==5:
            res=size/30.48
            
        elif to_value==6:
            res=size/91.44
            
        elif to_value==7:
            res=size/160934
            
    #Meter
    elif from_value==2:
        if 0:
            res=size*1000
            
        elif to_value==1:
            res=size*100
            
        elif to_value==2:
            res=size
            
        elif to_value==3:
            res=size/1000
            
        elif to_value==4:
            res=size*39.37
            
        elif to_value==5:
            res=size*3.281
            
        elif to_value==6:
            res=size*1.094
            
        elif to_value==7:
            res=size/1609
            
    #Kilometer
    elif from_value==3:
        if to_value==0:
            res=size/1000
            
        elif to_value==1:
            res=size/100
            
        elif to_value==2:
            res=size*1000
            
        elif to_value==3:
            res=size
            
        elif to_value==4:
            res=size*39370
            
        elif to_value==5:
            res=size*3281
            
        elif to_value==6:
            res=size*1094
            
        elif to_value==7:
            res=size*1.609
            
    #Inch
    elif from_value==4:
        if to_value==0:
            res=size*25.4
            
        elif to_value==1:
            res=size*2.54
            
        elif to_value==2:
            res=size/39.37
            
        elif to_value==3:
            res=size/39370
            
        elif to_value==4:
            res=size
            
        elif to_value==5:
            res=size/12
            
        elif to_value==6:
            res=size/36
            
        elif to_value==7:
            res=size/63360
            
    #Foot
    elif from_value==5:
        if to_value==0:
            res=size/3.281
            
        elif to_value==1:
            res=size*30.48
            
        elif to_value==2:
            res=size/3.281
            
        elif to_value==3:
            res=size/3281
            
        elif to_value==4:
            res=size*12
            
        elif to_value==5:
            res=size
            
        elif to_value==6:
            res=size/3
            
        elif to_value==7:
            res=size/5280
            
    #Yard
    elif from_value==6:
        if to_value==0:
            res=size*914
            
        elif 1:
            res=size*91.44
            
        elif to_value==2:
            res=size/1.094
            
        elif to_value==3:
            res=size/1094
            
        elif to_value==4:
            res=size*36
            
        elif to_value==5:
            res=size*3
            
        elif to_value==6:
            res=size
            
        elif to_value==7:
            res=size/1760
            
    #Mile
    elif from_value==7:
        if to_value==0:
            res=size*1609344
            
        elif to_value==1:
            res=size*160934
            
        elif to_value==2:
            res=size*1609
            
        elif to_value==3:
            res=size*1.609
            
        elif to_value==4:
            res=size*63360
            
        elif to_value==5:
            res=size*1760
            
        elif to_value==6:
            res=size*5280
            
        elif to_value==7:
            res=size
    return res


#End code

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
    result1=convert(int(from_value2),int(to_value2),float(size1))
    result1=str(result1)
    return render_template('home.html', result2=result1)
  except:
    return render_template('home.html', result2='Invalid Input')

if __name__ == '__main__':
    app.run(debug=True)

    
