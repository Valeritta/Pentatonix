from flask import Flask,  render_templates
app=Flask(__name__)

@app.route('/')
def connect1():
    return render_templates('index.html')

if (__name__=="__main__"):
    app.debug = True
    app.run