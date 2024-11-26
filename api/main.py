from flask import Flask
from bs4 import BeautifulSoup
from utils import htmlSearchToNovels
import requests
import json

SOURCE_ROOT = "https://novel-index.com"

app = Flask(__name__)

@app.route("/refresh_search/")
def refresh_search():
    r = requests.get(SOURCE_ROOT)
    doc = BeautifulSoup(r.text,"html.parser")
    html_novels = doc.find_all(class_="recherche")
    novels = htmlSearchToNovels(html_novels)

    with open("./novels.json", "w", encoding="utf8") as f:
        json.dump(novels, f, ensure_ascii=False)

    return str(novels)
    

@app.route("/search/<search_text>")
def search(search_text):
    novels = []
    with open("./novels.json", "r", encoding="utf8") as f:
        novels = json.load(f)
    
    filtered_novels = []

    for n in novels:
        if search_text in str.lower(n['name']):
            filtered_novels.append(n)

    return filtered_novels