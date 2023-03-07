from flask import Flask, render_template, request

main = Flask(__name__)

@main.route('/')
def hello_world():
    return 'Hello, World!'

@main.route('/hello', methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        name = request.form['name']
        return f'Hello, {name}!'
    else:
        return render_template('index.html')

if __name__ == '__main__':
    main.run()
