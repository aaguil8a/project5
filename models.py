from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///portfolio.db"
db = SQLAlchemy(app)


class Project(db.Model):

    __tablename__ = "project"

    id = db.Column("ID", db.Integer, primary_key=True)
    title = db.Column("Title", db.String())
    date_completed = db.Column("Date", db.Date)
    description = db.Column("Description", db.String())
    skills = db.Column("Skills Practiced", db.String())
    github = db.Column("GitHub Repo", db.String())

    def __repr__(self):
        
        return f""" Project ID: {self.id} | Project Title: {self.title} | Date Completed: {self.date_completed} 
                | {self.description} | Skills practiced: {self.skills_practiced} | Github Repo: {self.github}"""
