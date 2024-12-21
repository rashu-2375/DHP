from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/crop', methods=['GET', 'POST'])
def crop():
    if request.method == 'POST':
        # Handle the form submission for cropping
        # Example: Retrieve form data and perform cropping
        return redirect(url_for('index'))  # Redirect back to the index page after cropping
    return render_template('crop.html')

@app.route('/blur', methods=['GET', 'POST'])
def blur():
    if request.method == 'POST':
        # Handle the form submission for blurring
        # Example: Retrieve form data and perform blurring
        return redirect(url_for('index'))  # Redirect back to the index page after blurring
    return render_template('blur.html')
@app.route('/rotate', methods = ['GET', 'POST'])
def rotate():
    if request.method == 'POST':
        return redirect(url_for('index'))
    return render_template('rotate.html')

if __name__ == '__main__':
    app.run(debug=True)
