from flask import Flask, render_template

app = Flask(__name__, template_folder = 'frontend/templates', static_folder = 'frontend', static_url_path = '/static')        
app.config['TEMPLATES_AUTO_RELOAD'] = True

# app.config['SECRET_KEY'] = 'vasya'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///static/data/data.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@app.route('/')
def index():
    return render_template('index.jinja')

if __name__ == '__main__':
    app.run(debug = True)