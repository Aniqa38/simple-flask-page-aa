from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    books = ["To Kill a Mockingbird", "1984", "The Great Gatsby", "The Catcher in the Rye", "Moby Dick"]
    movies = ["The Shawshank Redemption", "The Godfather", "The Dark Knight", "Pulp Fiction", "Forrest Gump"]
    return render_template("index.html", books=books, movies=movies)

if __name__ == "__main__":
    app.run(debug=True)
