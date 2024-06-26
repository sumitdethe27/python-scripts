from flask import Flask,render_template, Response
import requests



app=Flask(__name__)

@app.route('/',methods=['GET'])
def welcome():
    response=requests.get('https://sumit27-portfolio.netlify.app/')
    res=Response(response.text,mimetype='text/html')
    print(res.status_code)
    res.status_code
    
    return res


