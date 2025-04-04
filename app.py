from flask import Flask, render_template, request
from recommender import recommend_assessments
from scraper import extract_text_from_url

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    results = []
    if request.method == 'POST':
        query = request.form['query']
        if query.startswith("http"):
            query = extract_text_from_url(query)
        results = recommend_assessments(query)
    return render_template('index.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
