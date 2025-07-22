from flask import Flask,request,render_template
app = Flask(__name__)
@app.route("/")
def welcome():
    return "<html> <H1> Welcome to the flask course </H1> </html>"

@app.route("/index",methods=['GET'])
@app.route('/form',methods =['GET','POST'])
def form():
    if request.methods =='POST':
        name=request.form['name']
        return f'hello {name}!'
    return render_template('form.html')

##Variable rule
@app.route('/success/<int:score>')
def success(score):
    return "the marks you got is "+ str(score)

##building URL dynamically
@app.route('/result/<int:score>')
def result(score):
    res =""
    if score>=50:
        res = "PASSED"
    else:
        res = "FAILED"
    return render_template('result.html',result=res)   

if __name__=="__main__":
    app.run(debug =  True)     




