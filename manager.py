from flask_script import Manager
from c2 import app

manager = Manager(app)

@manager.command
def hello(name):
    print 'hello',name

if __name__ == '__main__':
    manager.run()

