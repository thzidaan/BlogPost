## F - Flask

[Flask](https://flask.palletsprojects.com/en/1.1.x/) is a web server back-end framework.

Being built with Python in mind allows developers to quickly prototype and deploy solutions for tasks at hand. Providing a high level of abstraction means that REST api endpoints can be quickly built, tested and deployed. As well as with a large quantity of robust libraries for a myriad of tasks means that complex problems can be solved more efficiently by importing the necessary tools.

_A whole flask application can be made as simply as [below](https://palletsprojects.com/p/flask/)._

```python
from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'
```

## Dependencies

```python
pip install -r requirements.txt
```
