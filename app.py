from flask import Flask
from urllib.parse import quote  # Import quote from urllib.parse

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '''
<html>
<body>
<center>
<h1>welcome 2  kubernetes.</h1> <br>
<br>
<img src="https://github.com/vvarshney/argo-cd/blob/main/itsworking.jpeg?raw=true">
</center>
</body>
</html>
'''

# Rest of your Flask app code...

