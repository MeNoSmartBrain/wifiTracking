import folium
from folium.plugins import MarkerCluster

# Create a map object
m = folium.Map(location=[11.0, 11.0], zoom_start=13)

# Define the JavaScript function to create the icon
icon_create_function = '''
    function(cluster) {
        return L.divIcon({
            html: '<div class="circle-marker-cluster'''+str(cIndex)+'''">' +
                '<span>' + cluster.getChildCount() + '</span></div>',
            className: 'marker-cluster-custom',
            iconSize: new L.Point(40, 40)
        });
    }
'''

# Define the CSS styles for the custom icon
css_style = '''
    .circle-marker-cluster'''+str(cIndex)+''' {
        display: flex;
        align-items: center;
        justify-content: center;
        width: 40px;
        height: 40px;
        background-color: '''+ hexColors[cIndex] +''';
        border-radius: 50%;
        color: white;
        font-weight: bold;
        font-size: 14px;
    }
    .circle-marker-cluster'''+str(cIndex)+''' span {
        display: inline-block;
        margin-top: 2px;
    }
'''

# Add the custom CSS styles to the map
m.get_root().header.add_child(folium.Element('<style>{}</style>'.format(css_style)))

# Create a marker cluster with the custom icon function
marker_cluster = MarkerCluster(icon_create_function=icon_create_function)

# Add markers to the marker cluster
marker_cluster.add_child(folium.Marker(location=[11.0, 11.0]))
marker_cluster.add_child(folium.Marker(location=[11.0, 11.0]))
# Add more markers as needed

# Add the marker cluster to the map
m.add_child(marker_cluster)

# Display the map
map = m



# Save the map
map.save('test.html')




import webbrowser
webbrowser.open('test.html')