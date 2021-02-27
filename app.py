from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)


# Path of your database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(app)


class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(20), nullable=False, default='N/A')
    date_posted = db.Column(db.DataTime, nullable=False,
                            default=datetime.utcnow)

    def __repr__(self):
        return 'Blog post' + str(self.id)


all_posts = [
    {
        'title': 'Post 1',
        'content': 'This is the content of post 1',
        'author': 'Eren'

    },
    {
        'title': 'Post 2',
        'content': 'This is the content of post 2'

    }
]


@app.route('/home')
def index():
    return render_template("index.html")


@app.route('/posts')
def posts():
    return render_template('posts.html', posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
