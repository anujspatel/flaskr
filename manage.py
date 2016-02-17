#!/usr/bin/env python
import os, sys

from flask import Flask
import settings
from fuckr import app

app.config.from_object(settings)

if __name__ == '__main__':
	app.run()