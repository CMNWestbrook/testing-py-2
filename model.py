from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Game(db.Model):
    """Board game."""

    __tablename__ = "games"
    game_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), nullable=False, unique=True)
    description = db.Column(db.String(100))

# change it back to postgresql:///games for release
def connect_to_db(app, db_uri="postgresql:///games"):
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    db.app = app
    db.init_app(app)


def example_data():
    """Create example data for the test database."""

    cards_against_humanity = Game(name = 'cards against humanity', description = 'funny game')
    jinga = Game(name = 'jinga', description = 'knocking over game')
    #FIXME: write a function that creates a game and adds it to the database.
    # print "FIXME"

    db.session.add_all([cards_against_humanity, jinga])
    db.session.commit()
if __name__ == '__main__':
    from server import app

    connect_to_db(app)
    print "Connected to DB."
 