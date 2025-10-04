from flask import Flask,render_template,jsonify
from flask import request
import math

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def homepage():
    return render_template('file1_updated.html')


@app.route('/math',methods=['GET','POST'])
def math_operation():
    if request.method=='POST':
        ops=request.form['operation']
        num1=float(request.form['num1'])
        num2=float(request.form['num2'])
        
    if (ops=='add'):
        r=num1+num2
        result= 'sum is '+str( r)
        return render_template('file2_updated.html',result=result)
            
        
        
    elif(ops=='subtract'):
        r=num1-num2
        result ='subtract is '+str( r)
        return render_template('file2_updated.html',result=result)
        
        
        
    elif(ops=='multiply'):
        r=num1*num2
        result= 'multiply is '+str( r)
        return render_template('file2_updated.html',result=result)
        
        
        
    elif(ops=='divide'):
        r=num1/num2
        result= 'divide is '+str( r)
        return render_template('file2_updated.html',result=result)
        
       
        
    elif(ops=='log'):
        result= 'log is '+str(math.log(num1, num2) )
        return  render_template('file2_updated.html',result=result)
        

        
if __name__=='__main__':
    app.run(host='0.0.0.0')