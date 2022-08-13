from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.get('/shorten')
def shorten_get():
    return render_template('shorten.html')


@app.post('/shorten')
def shorten_post():
    url = request.form['url']
    if not url:
        return 'No URL provided'
    return render_template('shorten.html', url=url, surl='shortened_link')


if __name__ == '__main__':
    app.run(debug=True)
