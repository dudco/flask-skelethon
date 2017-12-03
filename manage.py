import json
from flask_script import Manager, prompt_bool
from flask_migrate import Migrate, MigrateCommand

from app import create_app, db
# from app.models import Exchange, Review, Comment, Post

app = create_app()
migrate = Migrate(db, app)
manager = Manager(app)

@MigrateCommand.command
def clear():
    "Clear DB"
    if prompt_bool("Are you sure you want to clear all your data"):
        meta = db.metadata
        for table in reversed(meta.sorted_tables):
            print ('Clear table %s' % table)
            db.session.execute(table.delete())
        db.session.commit()
        print('clear done')

@MigrateCommand.command
def drop():
    "Drop DB"
    if prompt_bool("Are you sure you want to drop all your data"):
        db.drop_all()


@MigrateCommand.command
def create():
    "Create DB"
    db.create_all()

@MigrateCommand.command
def dummy():
    "Make dummy data"
    print("Fill dummy data")

MyCommand = Manager(usage="MyCommand")

@MyCommand.command
def command():
    "Please fill commands"
    print("Please fill Commands")


manager.add_command('db', MigrateCommand)
manager.add_command('my', MyCommand)

@manager.command
def run():
    app.run(host=app.config['HOST'], port=app.config['PORT'], debug=app.debug, threaded=True)

if __name__ == '__main__':
    manager.run()
