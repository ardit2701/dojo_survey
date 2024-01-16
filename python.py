from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a random secret key for session

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')
    session['form_data'] = {'name': name, 'email': email, 'message': message}
    return redirect('/result')

@app.route('/result')
def result():
    form_data = session.get('form_data', {})
    return render_template('result.html', form_data=form_data)

if __name__ == '__main__':
    app.run(debug=True)
