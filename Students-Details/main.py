from flask import Flask, render_template, request, redirect

app=Flask(__name__)

studentData={}

@app.route('/insert',methods=['POST'])
def InsertData():
    name=request.form['name']
    rollNumber=request.form['rollNumber']
    age=request.form['age']
    gender=request.form['gender']
    studentData[rollNumber]=[name,age,gender]
    print studentData
    return ("<h1> data inserted </h1>")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/display',methods=['POST','GET'])
def displayData():
    return render_template('display.html',data=studentData)

@app.route('/delete',methods=['POST'])
def deleteData():
    rollNumber=request.form['rollNumber']
    studentData.pop(rollNumber)
    return ("<h1> data deleted </h1>")
    
@app.route('/update',methods=['POST'])
def updateData():
    name=request.form['name']
    rollNumber=request.form['rollNumber']
    age=request.form['age']
    gender=request.form['gender']
    if studentData.has_key(rollNumber):
        studentData[rollNumber]=[name,age,gender]
        return ('<h1>data updated</h1>')



if __name__=='__main__':
    app.run(debug=True)