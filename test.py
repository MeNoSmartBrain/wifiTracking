import folium
from folium.plugins import MarkerCluster

# Create a map object
m = folium.Map(location=[11.0, 11.0], zoom_start=13)

# Define the JavaScript function to create the icon
icon_create_function = '''
    function(cluster) {
        return L.divIcon({
            html: '<div style="background-color: red; color: white;">' +
                  cluster.getChildCount() + '</div>',
            className: 'marker-cluster-custom',
            iconSize: new L.Point(40, 40)
        });
    }
'''

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