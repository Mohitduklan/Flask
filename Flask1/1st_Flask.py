from flask import Flask, render_template, redirect, url_for, request, jsonify
import jsonFile
app = Flask(__name__)
print(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/success/<name>')
def success(name):
    userList = []
    for post in jsonFile.post:
        if name == post['name']:
            userList.append(post)
    return render_template('home.html', posts=userList)

def check(user):
    nameList = [jsonFile.post[i]['name'] for i in range(len(jsonFile.post))]
    if user in nameList:
        return True
    return False
        
@app.route("/login", methods = ['POST'])
def login():
    user = request.form['getName']
    valid = check(user)
    if valid == True:
        return redirect(url_for('success', name=user))
    return 'Not a user!!!!'

if __name__ == '__main__':
    app.run(debug=True, port=5000)
