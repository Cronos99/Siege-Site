from app import app, maps
from flask import render_template
import os

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', maps=maps)

@app.route('/<mapname>')
def user(mapname):
    
    path = './app/'
    sec_path = '../../app/'
    sites = []
    site = 0
    completeSites = []
    imageUrls = {}

    if mapname != 'favicon.ico':
        for dirname in os.listdir(path + mapname):
            complete = os.path.join(path, mapname, dirname)
            if os.path.isdir(complete):
                sites.append(dirname)
                completeSites.append(complete)

                for filename in os.listdir(complete):
                    if site in imageUrls:
                        imageUrls[site].append(filename)
                    else:
                        imageUrls.setdefault(site, [filename])
            
                site += 1


        

    return render_template('default_map.html', map=mapname, sites=sites, imageUrls = imageUrls)