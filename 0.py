import folium

map = folium.Map(
    location= [-6.302403, 106.652248],
    zoom_start= 25
)
folium.Marker(
    [-6.302403, 106.652248],
    popup= '<b>Purwadhika</b>',
    tooltip= 'I am Here !!'    
).add_to(map)

map.save('1.html')