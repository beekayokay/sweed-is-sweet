from flask import Flask, render_template, url_for

app = Flask(__name__)

temp_posts = [
    {
        'author': 'Brian Ko',
        'title': 'Post 1',
        'content': f'{"First post " * 100}',
        'date_posed': 'March 01, 2020'
    },
    {
        'author': 'Brian Ko',
        'title': 'Post 2',
        'content': f'{"Second post " * 1000}',
        'date_posed': 'March 02, 2020'
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=temp_posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)
