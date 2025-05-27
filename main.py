import os
from dotenv import load_dotenv
from flask import Flask, render_template, request
import requests

load_dotenv()

app = Flask(__name__)

header = {"Authorization": f"Bearer {os.getenv('TOKEN')}"}

# You can create your own TOKEN(API-key) here -> https://the-one-api.dev/sign-up  !!!(for model only)!
# For more information visit Documentation    -> https://the-one-api.dev/documentation

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/book', methods=["GET"])
def get_all_books():
    response = requests.get(url="https://the-one-api.dev/v2/book").json()
    books = response['docs']
    return render_template("book.html", books=books)


@app.route('/book/{identity}', methods=['GET'])
def get_a_book():
    response = requests.get(url=f"https://the-one-api.dev/v2/book/{request.args.get('identity')}").json()
    book = response['docs'][0]
    return render_template("book_data.html", book=book)


@app.route('/book/{identity}/chapter', methods=['GET'])
def get_chapters_by_book():
    response = requests.get(url=f"https://the-one-api.dev/v2/book/{request.args.get('identity')}/chapter").json()
    chapters = response['docs']
    book = requests.get(url=f"https://the-one-api.dev/v2/book/{request.args.get('identity')}").json()['docs'][0]
    return render_template("book_by_chapter.html", chapters=chapters, book=book)


@app.route('/movie', methods=["GET"])
def get_all_movies():
    response = requests.get(url="https://the-one-api.dev/v2/movie", headers=header).json()
    movies = response['docs']
    return render_template("movie.html", movies=movies)


@app.route('/movie/{identity}', methods=["GET"])
def get_movie_data():
    response = requests.get(url=f"https://the-one-api.dev/v2/movie/{request.args.get('identity')}", headers=header).json()
    data = response['docs'][0]
    return render_template("movie_data.html", movie_data=data)


@app.route('/character', methods=["GET"])
def get_all_characters():
    response = requests.get(url="https://the-one-api.dev/v2/character", headers=header).json()
    characters_data = response['docs']
    return render_template("character.html", characters=characters_data)

@app.route('/character/{identity}', methods=["GET"])
def get_character_data():
    response = requests.get(url=f"https://the-one-api.dev/v2/character/{request.args.get('identity')}", headers=header).json()
    character_data = response['docs'][0]
    return render_template("character_data.html", character_data=character_data)


@app.route('/quote', methods=["GET"])
def get_all_quotes():
    response = requests.get(url="https://the-one-api.dev/v2/quote", headers=header).json()
    quotes = response['docs']
    return render_template("quote.html", quotes=quotes)


@app.route('/quote/{identity}', methods=["GET"])
def get_quote_data():
    response = requests.get(url=f"https://the-one-api.dev/v2/quote/{request.args.get('identity')}", headers=header).json()
    quote_data = response['docs'][0]
    return render_template("quote_data.html", quote_data=quote_data)

#
# @app.route('/movie/{identity}/quote', methods=["GET"])
# def get_all_quotes_in_movie():
#     response = requests.get(url=f"https://the-one-api.dev/v2/movie/{request.args.get('identity')}/quote", headers=header).json()
#     quotes = response['docs']
#     movie = requests.get(url=f"https://the-one-api.dev/v2/movie/{request.args.get('identity')}", headers=header).json()['docs'][0]
#
#     return render_template("quotes_by_movie.html", quotes=quotes, movie=movie)


@app.route('/chapter', methods=["GET"])
def get_all_chapters():
    response = requests.get(url="https://the-one-api.dev/v2/chapter", headers=header).json()
    chapters = response['docs']
    return render_template("chapter.html", chapters=chapters)



if __name__ == "__main__":
    app.run(debug=True)
