#!/usr/bin/env python
from flask.ext.script import Manager
from fuckr import app

manager = Manager(app)

if __name__ == "__main__":
	fuckr.init_db()
    manager.run()