from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/temperature', methods=['POST'])

def temperature():
 
 Location = request.form['Location']
 r = requests.get("http://api.openweathermap.org/data/2.5/weather?APPID=eb951c690cc14f214a3768ed97e51cd7&q=" + Location)
 json_object = r.json()
 temp_k = float(json_object['main']['temp'])
 temp_c_raw = temp_k - 273
 temp_c = round(temp_c_raw, 1)
 #weather = (json_object['weather']['description'])
 return render_template('temperature.html', temp=temp_c)
 


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
