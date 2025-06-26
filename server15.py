from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('project7form.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    message=request.form['message']
    
    if not name or not email:
        return "Enter details"
    
    data = {
        "name": name,
        "email": email,
        "message":message,
    }
    return render_template("project7result.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)
