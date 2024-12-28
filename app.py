from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

df = pd.read_csv('data/movies.csv')

@app.route('/')
def home():
    return render_template('home.html', movies = df.to_dict(orient='records'))

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('q', '').lower()
    filtered_movies= df[df['Title'].str.contains(query, case=False)]
    return render_template('home.html', movies = filtered_movies.to_dict(orient='records'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=False)