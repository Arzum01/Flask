import flask
from flask import Flask
app = Flask(__name__)
skills = ["math", "programming", "language learning", "critical thinking", "playing piano"]

students = {
    "1": "Deniz",
    "2": "Muzeffer",
    "3": "Aytac",
    "4": "Gulxanim",
    "5": "Baloglan"
}

@app.route("/")
def greet():
    return "Welcome to My Portfolio"

@app.route("/about")
def about_me():
    return "Salam! Mən Əkbərli Arzum. Hal-hazırda Azərbaycan Dövlət İqtisad Universitetinin Rəqəmsal İqtisadiyyat fakültəsinin Kompüter Elmləri ixtisasında təhsil alıram. Təmkinli, çalışqan, ideallığa can atan bir tələbəyəm. Özümü inkişaf etdirmək məqsədilə Coursera platformasında kurslar götürürəm. Xarici dillərə marağım hədsizdir. Sərbəst şəkildə ingilis və rus dillərində danışa bilirəm və alman dilini orta səviyyәdә bilirәm. Bundan әlavә bir-sıra könüllülük proqramlarına müraciәt edirәm. Tәzәlikcә A-level education kömәkliyi ilә Leadership Volunteering Summit-dә töhfәm olub. Boş vaxlarımı voleybol oynamaqla vә ya piano çalmaqla dәyәrlәndirirәm."

@app.route("/skills")
def skill():
    for i in skills:
        html = "<ul>"
        for i in skills:
            html+= f"<li>{i}</li>"
        html+= "</ul>"
        return html

@app.route("/profile/<username>")
def salamla(username):
    return f"Welcome {username}!"

@app.route("/student/<int:id>")
def student_name(id):
    for key, value in students.items():
        if str(id) == key:
            return value
        
    return "Student Not Found"

@app.route("/sum/<int:a>/<int:b>")
def sum(a,b):
    s = a+b
    return str(s)

app.run(debug=True)