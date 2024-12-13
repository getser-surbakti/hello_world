from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    initial_investment = float(request.form['initial_investment'])
    final_value = float(request.form['final_value'])
    time_period = float(request.form['time_period'])

    # Calculate the return on investment (ROI)
    roi = (final_value - initial_investment) / initial_investment
    annualized_roi = (1 + roi) ** (1 / time_period) - 1

    return render_template('result.html', roi=roi, annualized_roi=annualized_roi)

if __name__ == '__main__':
    app.run(debug=True)
