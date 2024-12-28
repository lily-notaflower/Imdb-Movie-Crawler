from flask import Flask, render_template, request
import pandas as pd
import os

app = Flask(__name__)

DATA_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'movies.csv')
df = pd.read_csv(DATA_PATH)

@app.route('/')
def home():
    return render_template('home.html', movies = df.to_dict(orient='records'))

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('q', '').lower()
    filtered_movies= df[df['Title'].str.contains(query, case=False)]
    return render_template('home.html', movies = filtered_movies.to_dict(orient='records'))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)