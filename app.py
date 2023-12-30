from flask import Flask
from urllib.parse import quote  # Import quote from urllib.parse

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '''
<html>
<bodhi<h1>
<center>
<h1>welcome to kubernetes.</h1> <br>
<br>
<img src="https://github.com/kamnigs1993/argo-cd/blob/main/itsworking.jpeg?raw=true">
</center>
</body>
</html>
'''

# Rest of your Flask app code...

