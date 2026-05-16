from flask import Flask, render_template, request, redirect, session
import json
import os

app = Flask(__name__)
app.secret_key = "library123"

# ---------------- DATA ----------------
BOOKS_FILE = "books.txt"


def load_books():
    if not os.path.exists(BOOKS_FILE):
        return []

    loaded_books = []
    with open(BOOKS_FILE, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            try:
                loaded_books.append(json.loads(line))
            except json.JSONDecodeError:
                continue
    return loaded_books


def save_books():
    with open(BOOKS_FILE, "w", encoding="utf-8") as file:
        for book in books:
            file.write(json.dumps(book) + "\n")


books = load_books()
members = [{"id": "101", "name": "Demo User"}]
issued = []

roles = {"admin": "admin123"}


# ---------------- HOME ----------------
@app.route("/")
def home():
    return render_template("index.html")


# ---------------- LOGIN ----------------
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        role = request.form["role"]
        user_id = request.form["user_id"]
        password = request.form["password"]

        if role == "admin" and password == roles["admin"]:
            session["role"] = "admin"
            return redirect("/admin")

        if role == "member":
            if any(m["id"] == user_id for m in members):
                session["role"] = "member"
                session["user_id"] = user_id
                return redirect("/member")

        return "Invalid Login"

    return render_template("login.html")


# ---------------- ADMIN ----------------
@app.route("/admin")
def admin():
    return render_template("admin.html", books=books)


@app.route("/add_book", methods=["GET", "POST"])
def add_book():
    if request.method == "POST":
        book = {
            "acc": request.form["acc"],
            "title": request.form["title"],
            "author": request.form["author"],
            "category": request.form["category"],
            "copies": int(request.form["copies"]),
            "available": int(request.form["copies"])
        }
        books.append(book)
        save_books()
        return redirect("/admin")

    return render_template("add_book.html")


@app.route("/delete/<acc>")
def delete(acc):
    global books
    books = [b for b in books if b["acc"] != acc]
    save_books()
    return redirect("/admin")


# ---------------- SEARCH ----------------
@app.route("/search", methods=["GET", "POST"])
def search():
    result = []
    if request.method == "POST":
        key = request.form["key"].lower()
        result = [b for b in books if key in b["title"].lower()]
    return render_template("search.html", result=result)


# ---------------- MEMBER ----------------
@app.route("/member")
def member():
    return render_template("member.html", books=books)


@app.route("/issue/<acc>")
def issue(acc):
    user = session.get("user_id")

    for b in books:
        if b["acc"] == acc and b["available"] > 0:
            b["available"] -= 1
            issued.append({"acc": acc, "user": user})
            save_books()
            break

    return redirect("/member")


@app.route("/return/<acc>")
def return_book(acc):
    user = session.get("user_id")

    for i in issued:
        if i["acc"] == acc and i["user"] == user:
            issued.remove(i)
            for b in books:
                if b["acc"] == acc:
                    b["available"] += 1
                    save_books()
                    break
            break

    return redirect("/member")


# ---------------- RUN ----------------
# if __name__ == "__main__":
#     app.run(debug=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
