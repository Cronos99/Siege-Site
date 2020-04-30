from flask import Flask

app = Flask(__name__)

maps = ['Border', 'Chalet']


from app import routes