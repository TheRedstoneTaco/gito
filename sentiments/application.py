from flask import Flask, redirect, render_template, request, url_for

import helpers
from analyzer import Analyzer

import os
import sys

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search")
def search():

    # validate screen_name
    screen_name = request.args.get("screen_name", "")
    if not screen_name:
        return redirect(url_for("index"))

    # get screen_name's last 50 tweets
    tweets = helpers.get_user_timeline(screen_name, 50)
    if not tweets:
        sys.exit("sorry no tweets found")

    # set up for analyzing and counting
    positive, negative, neutral = 0.0, 0.0, 0.0
    positives = os.path.join(sys.path[0], "positive-words.txt")
    negatives = os.path.join(sys.path[0], "negative-words.txt")
    analyzer = Analyzer(positives, negatives)
    # analyze and count each tweet
    for tweet in tweets:
        curScore = analyzer.analyze(tweet)
        if curScore > 0.0:
            positive += 1
        elif curScore < 0.0:
            negative += 1
        else:
            neutral += 1

    # generate chart
    chart = helpers.chart(positive, negative, neutral)

    # render results
    return render_template("search.html", chart=chart, screen_name=screen_name)
