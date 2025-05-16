from flask import Flask, render_template

app = Flask(__name__)

@app.route('/usuario_create')
def usuario_create():
    return render_template('usuario_create.html')

if __name__ == '__main__':
    app.run(debug=True)

