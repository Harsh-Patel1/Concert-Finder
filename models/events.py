from app import db  # Assuming 'db' is the SQLAlchemy instance

class Events(db.Model):
    EventID = db.Column(db.Integer, primary_key=True)
    Title = db.Column(db.String(255), unique=True, nullable=False)
    EventDate = db.Column(db.Date, unique=True, nullable=False)
    Program = db.Column(db.String)
    Poster = db.Column(db.String)

'''
SQL-esque version of the above Pythion-esque table creation code

CREATE TABLE Events (
    EventID INT PRIMARY KEY AUTO_INCREMENT,
    Title VARCHAR(255) NOT NULL,
    EventDate DATE NOT NULL,
    Program VARCHAR(255) --the file path to a program
    Poster VARCHAR(255) --file path to poster
)
'''