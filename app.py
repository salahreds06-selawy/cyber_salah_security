from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/journey')
def journey():
    return render_template('journey.html')

@app.route('/knowledge')
def knowledge():
    return render_template('knowledge.html')

@app.route('/hacking_tools')
def hacking_tools():
    return render_template('hacking_tools.html')

@app.route('/roadmaps')
def roadmaps():
    return render_template('roadmaps.html')

@app.route('/connect')
def connect():
    return render_template('connect.html')

@app.route('/search')
def search():
    query = request.args.get('q', '').lower()
    if 'nmap' in query:
        return render_template('nmap_tutorial.html')
    elif 'tor' in query:
        return render_template('tor_guide.html')
    else:
        return "<h2 style='color:red; text-align:center;'>❌ لم نعثر على نتيجة</h2>"

@app.route('/beginner_path')
def beginner_path():
    return render_template('beginner_path.html')

@app.route('/intermediate_path')
def intermediate_path():
    return render_template('intermediate_path.html')

@app.route('/advanced_path')
def advanced_path():
    return render_template('advanced_path.html')

@app.route('/tor_guide')
def tor_guide():
    return render_template('tor_guide.html')

@app.route('/lab')
def lab():
    return render_template('lab.html')

@app.route('/vault')
def vault():
    return render_template('vault.html')

if __name__ == '__main__':
    app.run(debug=True)
