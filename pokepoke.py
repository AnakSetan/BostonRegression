import folium
from flask import Flask,render_template,redirect,abort
import pandas as pd
import numpy as np

# print(df)
#-------------------------------------------------
# df = pd.read_csv('pokemon-spawns.csv')
# print(df.iloc[0:100])#mengambil sample berjumlah 100
app = Flask(__name__)
@app.route('/')
def home():
    df = pd.read_csv('pokemon-spawns.csv', index_col= False)
    map = folium.Map(
        location= [df.iloc[0]['lat'],df.iloc[0]['lng']],
        zoom_start= 15
    )
    for i in range(len(df.iloc[0:100])):
        folium.Marker(
            [(df.iloc[i]['lat']),(df.iloc[i]['lng'])],
            popup=df.iloc[i]['name'],
            tooltip=df.iloc[i]['name']
        ).add_to(map)
    map.save('templates/pokemon.html')
    return render_template('pokemon.html')

@app.route('/map')
def map():
    return render_template('pokemon.html')
if __name__ == '__main__':
    app.run(debug = True)