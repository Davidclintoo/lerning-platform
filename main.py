from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def home_page():
    return render_template('index.html')

@app.route('/software')
def software_page():
   
    return render_template('software.html')

@app.route('/machine_learning')
def ml_page():
   
    return render_template('ml.html')

@app.route('/artificial_intelligence')
def al_page():
   
    return render_template('ai.html')

@app.route('/mechanical')
def mechanical_page():
   
    return render_template('mechanical.html')

@app.route('/soft-mech')
def soft_mech_page():
   
    return render_template('soft-mech.html')

@app.route('/project')
def project_page():
   
    return render_template('project.html')

@app.route('/css')
def css_page():
   
    return render_template('css.html')

@app.route('/python')
def python_page():
   
    return render_template('python.html')

app.run(debug=True)