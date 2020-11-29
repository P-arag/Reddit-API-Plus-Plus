from scraper import get_data
from flask import Flask, jsonify, render_template

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/api/<string:subredditName>')
def displayData(subredditName):
    postsData = get_data(subredditName)
    result = {
        "Developer": "Parag Jyoti Pal",
        "subreddit": subredditName + ", This api has been developed by Parag Jyoti Pal",
        "total_members": postsData[0],
        "active_users": postsData[1],
        "posts": postsData[2]
    }
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)
