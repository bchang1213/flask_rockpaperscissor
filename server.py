from flask import Flask, render_template, session, redirect
import random

app = Flask(__name__)
app.secret_key = 's@54e236ecr8v0x8972f@#$5vs!$'

@app.route("/")