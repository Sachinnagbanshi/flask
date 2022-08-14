#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask,render_template,request
app=Flask(__name__)
@app.route('/')
def fkjfkj():
    return render_template('sumprog.html')
@app.route('/info',methods=['POST'])
def fkjfkjff():
    if(request.method=='POST'):
        num1=float(request.form['a'])
        num2=float(request.form['b'])
        result=num1+num2
        return render_template('sumprog.html',answer=result)
if __name__=='__main__':
    app.run()
