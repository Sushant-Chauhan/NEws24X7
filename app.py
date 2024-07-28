from flask import Flask, render_template
import requests
app = Flask(__name__)
app.secret_key = "#$r59gnvk5^&@#0-m_6edn$%"

@app.route('/') 
def index():
    # url = "https://newsapi.org/v2/everything?q=technology&from=2024-07-27&to=2024-07-27&sortBy=popularity&apiKey=5bebd4e1547f4cfe969673a6eb70d708"         # everything?q=BITCOIN/sports/politics/agriculture/etc.
    url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=5bebd4e1547f4cfe969673a6eb70d708"     # TOP-HEADLINES


    r = requests.get(url).json()
    case = {
        'articles' : r['articles']
    }
    return render_template("index.html", cases = case)

if __name__ == '__main__':
    app.run(debug=True, port=5002)
