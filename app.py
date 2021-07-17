import flask
from flask import Flask, render_template, request
from question import Question
from database import db

'''Create a flask application instance using this file.'''
app = Flask(__name__)

'''Tell the webapp where the db is located.'''
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///questions.db'

'''Import an empty SQLite db and register with this app.'''
db.init_app(app)

'''Create the columns of the db within the context of this application.'''
with app.app_context():
    db.create_all()



''''''
@app.route('/', methods = ["POST", "GET"])
def index():
    if request.method == "POST":
        # POST
        task_content = request.form["content"]
        new_question = Question(content = task_content)

        # push the data to db
        try:
            db.session.add(new_question)
            db.session.commit()
            return flask.redirect("/")
        except:
            return "An error encountered while trying to add the question to the database."

    else:
        # GET
        questions = Question.query.order_by(Question.date_saved).all()
        return render_template("index.html", questions = questions)


@app.route("/delete/<int:id>")
def delete(id):
    entry_to_delete = Question.query.get_or_404(id)

    try:
        db.session.delete(entry_to_delete)
        db.session.commit()
        return flask.redirect("/")
    except:
        return "An error encountered while trying to delete the question."


@app.route("/update/<int:id>", methods = ["Get", "POST"])
def update(id):
    question_to_update = Question.query.get_or_404(id)
    if request.method == "POST":
        question_to_update.content = request.form["content"]

        try:
            db.session.commit()
            return flask.redirect("/")
        except:
            return "An error encountered while trying to update the question."


    else:
        return render_template("update.html", question = question_to_update)



if __name__ == "__main__":
    app.run(debug = True)