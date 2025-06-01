from flask import Flask, render_template, url_for, request

app = Flask(__name__)


@app.route('/', methods=['POST','GET'])
def index():
    result = None

    if request.method == 'POST':
        equation = request.form.get('equation')

        try:
            result=eval(equation)
        except Exception as e:
            result=f"Error: {e}"

    return render_template('calc.html',result=result)

if __name__ == "__main__":
    app.run(debug=True)
