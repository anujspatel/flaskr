#!/usr/bin/env python
import os, sys

import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from contextlib import closing
from fuckr import app

if __name__ == '__main__':
	app.run()