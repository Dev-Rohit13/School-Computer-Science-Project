import folium
import webbrowser

map_center = [30, 0]
zoom_start = 2

class Map: 
    def __init__(self, center, zoom_start):
        self.center = center
        self.zoom_start = zoom_start

    def showMap(self, world_map):
        # Create the map
        world_map.save("map_b.html")
        webbrowser.open("map_b.html")

spending_data = {
    'Iran': {'Refugee spending': 10000000, 'Foreign affairs spending': 20000000, 'Latitude': 35.6892, 'Longitude': 51.3890},
    'Ethiopia': {'Refugee spending': 5000000, 'Foreign affairs spending': 10000000, 'Latitude': 9.1450, 'Longitude': 40.4897},
    'Bangladesh': {'Refugee spending': 8000000, 'Foreign affairs spending': 15000000, 'Latitude': 23.8103, 'Longitude': 90.4125},
    'Sudan': {'Refugee spending': 3000000, 'Foreign affairs spending': 6000000, 'Latitude': 15.5007, 'Longitude': 32.5599},
    'Poland': {'Refugee spending': 2000000, 'Foreign affairs spending': 4000000, 'Latitude': 52.2297, 'Longitude': 21.0122},
    'Russia': {'Refugee spending': 15000000, 'Foreign affairs spending': 25000000, 'Latitude': 55.7558, 'Longitude': 37.6173},
    'Uganda': {'Refugee spending': 4000000, 'Foreign affairs spending': 8000000, 'Latitude': 0.3476, 'Longitude': 32.5825},
    'Pakistan': {'Refugee spending': 6000000, 'Foreign affairs spending': 12000000, 'Latitude': 33.7294, 'Longitude': 73.0931},
    'Germany': {'Refugee spending': 7000000, 'Foreign affairs spending': 14000000, 'Latitude': 52.5200, 'Longitude': 13.4050},
    'Turkey': {'Refugee spending': 9000000, 'Foreign affairs spending': 18000000, 'Latitude': 41.0082, 'Longitude': 28.9784},
    'India': {'Refugee spending': 11000000, 'Foreign affairs spending': 22000000, 'Latitude': 28.6139, 'Longitude': 77.2090},
    'United States': {'Refugee spending': 12000000, 'Foreign affairs spending': 24000000, 'Latitude': 38.9072, 'Longitude': -77.0369},
    'Brazil': {'Refugee spending': 13000000, 'Foreign affairs spending': 26000000, 'Latitude': -15.7942, 'Longitude': -47.8825},
    'China': {'Refugee spending': 14000000, 'Foreign affairs spending': 28000000, 'Latitude': 39.9042, 'Longitude': 116.4074},
    'Indonesia': {'Refugee spending': 15000000, 'Foreign affairs spending': 30000000, 'Latitude': -6.1751, 'Longitude': 106.8650},
    'Nigeria': {'Refugee spending': 16000000, 'Foreign affairs spending': 32000000, 'Latitude': 9.0578, 'Longitude': 7.4951},
    'Japan': {'Refugee spending': 17000000, 'Foreign affairs spending': 34000000, 'Latitude': 35.6895, 'Longitude': 139.6917},
    'Mexico': {'Refugee spending': 18000000, 'Foreign affairs spending': 36000000, 'Latitude': 19.4326, 'Longitude': -99.1332},
    'France': {'Refugee spending': 19000000, 'Foreign affairs spending': 38000000, 'Latitude': 48.8566, 'Longitude': 2.3522},
    'United Kingdom': {'Refugee spending': 20000000, 'Foreign affairs spending': 40000000, 'Latitude': 51.5074, 'Longitude': -0.1278},
    'Italy': {'Refugee spending': 21000000, 'Foreign affairs spending': 42000000, 'Latitude': 41.9028, 'Longitude': 12.4964},
    'South Africa': {'Refugee spending': 22000000, 'Foreign affairs spending': 44000000, 'Latitude': -25.7461, 'Longitude': 28.1881},
    'South Korea': {'Refugee spending': 23000000, 'Foreign affairs spending': 46000000, 'Latitude': 37.5665, 'Longitude': 126.9780},
    'Canada': {'Refugee spending': 24000000, 'Foreign affairs spending': 48000000, 'Latitude': 45.4215, 'Longitude': -75.6972},
    'Australia': {'Refugee spending': 25000000, 'Foreign affairs spending': 50000000, 'Latitude': -35.2809, 'Longitude': 149.1300},
    'Argentina': {'Refugee spending': 26000000, 'Foreign affairs spending': 52000000, 'Latitude': -34.6037, 'Longitude': -58.3816},
    'Spain': {'Refugee spending': 27000000, 'Foreign affairs spending': 54000000, 'Latitude': 40.4168, 'Longitude': -3.7038},
    'Ukraine': {'Refugee spending': 28000000, 'Foreign affairs spending': 56000000, 'Latitude': 50.4501, 'Longitude': 30.5234},
    'Colombia': {'Refugee spending': 29000000, 'Foreign affairs spending': 58000000, 'Latitude': 4.7100, 'Longitude': -74.0721},
    'Netherlands': {'Refugee spending': 30000000, 'Foreign affairs spending': 60000000, 'Latitude': 52.3702, 'Longitude': 4.8952},
    'Saudi Arabia': {'Refugee spending': 31000000, 'Foreign affairs spending': 62000000, 'Latitude': 24.7136, 'Longitude': 46.6753},
    'Egypt': {'Refugee spending': 32000000, 'Foreign affairs spending': 64000000, 'Latitude': 30.0444, 'Longitude': 31.2357},
    'Peru': {'Refugee spending': 33000000, 'Foreign affairs spending': 66000000, 'Latitude': -12.0464, 'Longitude': -77.0428},
    'Iraq': {'Refugee spending': 34000000, 'Foreign affairs spending': 68000000, 'Latitude': 33.3128, 'Longitude': 44.3615},
    'Philippines': {'Refugee spending': 35000000, 'Foreign affairs spending': 70000000, 'Latitude': 14.5995, 'Longitude': 120.9842},
    'Thailand': {'Refugee spending': 36000000, 'Foreign affairs spending': 72000000, 'Latitude': 13.7563, 'Longitude': 100.5018},
    'Sweden': {'Refugee spending': 37000000, 'Foreign affairs spending': 74000000, 'Latitude': 59.3293, 'Longitude': 18.0686},
    'Norway': {'Refugee spending': 38000000, 'Foreign affairs spending': 76000000, 'Latitude': 59.9139, 'Longitude': 10.7522},
    'Belgium': {'Refugee spending': 39000000, 'Foreign affairs spending': 78000000, 'Latitude': 50.8503, 'Longitude': 4.3517},
    'Switzerland': {'Refugee spending': 40000000, 'Foreign affairs spending': 80000000, 'Latitude': 46.9479, 'Longitude': 7.4474},
    'Austria': {'Refugee spending': 41000000, 'Foreign affairs spending': 82000000, 'Latitude': 48.2082, 'Longitude': 16.3738},
    'Denmark': {'Refugee spending': 42000000, 'Foreign affairs spending': 84000000, 'Latitude': 55.6761, 'Longitude': 12.5683},
    'Finland': {'Refugee spending': 43000000, 'Foreign affairs spending': 86000000, 'Latitude': 60.1699, 'Longitude': 24.9384},
    'Israel': {'Refugee spending': 44000000, 'Foreign affairs spending': 88000000, 'Latitude': 31.7683, 'Longitude': 35.2137},
    'Greece': {'Refugee spending': 45000000, 'Foreign affairs spending': 90000000, 'Latitude': 37.9838, 'Longitude': 23.7275},
    'Czech Republic': {'Refugee spending': 46000000, 'Foreign affairs spending': 92000000, 'Latitude': 50.0755, 'Longitude': 14.4378},
    'Portugal': {'Refugee spending': 47000000, 'Foreign affairs spending': 94000000, 'Latitude': 38.7223, 'Longitude': -9.1393},
    'Hungary': {'Refugee spending': 48000000, 'Foreign affairs spending': 96000000, 'Latitude': 47.4979, 'Longitude': 19.0402},
    'Ireland': {'Refugee spending': 49000000, 'Foreign affairs spending': 98000000, 'Latitude': 53.3498, 'Longitude': -6.2603},
    'Romania': {'Refugee spending': 50000000, 'Foreign affairs spending': 100000000, 'Latitude': 44.4268, 'Longitude': 26.1025},
    'New Zealand': {'Refugee spending': 51000000, 'Foreign affairs spending': 102000000, 'Latitude': -41.2865, 'Longitude': 174.7762},
    'Singapore': {'Refugee spending': 52000000, 'Foreign affairs spending': 104000000, 'Latitude': 1.3521, 'Longitude': 103.8198},
    'Malaysia': {'Refugee spending': 53000000, 'Foreign affairs spending': 106000000, 'Latitude': 3.1390, 'Longitude': 101.6869},
    'Venezuela': {'Refugee spending': 54000000, 'Foreign affairs spending': 108000000, 'Latitude': 10.4806, 'Longitude': -66.9036},
    'Chile': {'Refugee spending': 55000000, 'Foreign affairs spending': 110000000, 'Latitude': -33.4489, 'Longitude': -70.6693},
    'Kazakhstan': {'Refugee spending': 56000000, 'Foreign affairs spending': 112000000, 'Latitude': 51.1605, 'Longitude': 71.4704},
    'Morocco': {'Refugee spending': 57000000, 'Foreign affairs spending': 114000000, 'Latitude': 31.6295, 'Longitude': -7.9811},
    'Algeria': {'Refugee spending': 58000000, 'Foreign affairs spending': 116000000, 'Latitude': 36.7538, 'Longitude': 3.0588},
    'Vietnam': {'Refugee spending': 59000000, 'Foreign affairs spending': 118000000, 'Latitude': 21.0285, 'Longitude': 105.8542},
    'Tanzania': {'Refugee spending': 60000000, 'Foreign affairs spending': 120000000, 'Latitude': -6.7924, 'Longitude': 39.2083},
    'Kenya': {'Refugee spending': 61000000, 'Foreign affairs spending': 122000000, 'Latitude': -1.2921, 'Longitude': 36.8219},
    'Angola': {'Refugee spending': 62000000, 'Foreign affairs spending': 124000000, 'Latitude': -8.8390, 'Longitude': 13.2894},
    'Ghana': {'Refugee spending': 63000000, 'Foreign affairs spending': 126000000, 'Latitude': 5.5600, 'Longitude': -0.2057},
    'Zimbabwe': {'Refugee spending': 64000000, 'Foreign affairs spending': 128000000, 'Latitude': -17.8292, 'Longitude': 31.0521},
    'Tunisia': {'Refugee spending': 65000000, 'Foreign affairs spending': 130000000, 'Latitude': 36.8065, 'Longitude': 10.1815},
    'Jordan': {'Refugee spending': 66000000, 'Foreign affairs spending': 132000000, 'Latitude': 31.9454, 'Longitude': 35.9284},
    'Lebanon': {'Refugee spending': 67000000, 'Foreign affairs spending': 134000000, 'Latitude': 33.8938, 'Longitude': 35.5018},
}

refugee_data = {
    'Iran': {'Refugee population': (1200000/2)},
    'Ethiopia': {'Refugee population': (800000/2)},
    'Bangladesh': {'Refugee population': (900000/2)},
    'Sudan': {'Refugee population': (700000/2)},
    'Poland': {'Refugee population': (10000/2)},
    'Russia': {'Refugee population': (100000/2)},
    'Uganda': {'Refugee population': (1100000/2)},
    'Pakistan': {'Refugee population': (1600000/2)},
    'Germany': {'Refugee population': (600000/2)},
    'Turkey': {'Refugee population': (3600000/2)}
}

refugee_data_two = {
    'Iran': {'Refugee population': 1200000},
    'Ethiopia': {'Refugee population': 800000},
    'Bangladesh': {'Refugee population': 900000},
    'Sudan': {'Refugee population': 700000},
    'Poland': {'Refugee population': 10000},
    'Russia': {'Refugee population': 100000},
    'Uganda': {'Refugee population': 1100000},
    'Pakistan': {'Refugee population': 1600000},
    'Germany': {'Refugee population': 600000},
    'Turkey': {'Refugee population': 3600000}
}
# Calculate the total number of refugees in the top ten countries
total_refugees_top_ten = sum(refugee_data[country]['Refugee population'] for country in ['Iran', 'Ethiopia', 'Bangladesh', 'Sudan', 'Poland', 'Russia', 'Uganda', 'Pakistan', 'Germany', 'Turkey'])

# Calculate the number of refugees to be redistributed to each country


# Create a new dictionary with the redistributed refugee population
refugee_data_redistributed = {
    'Canada': {'Refugee population': 2270000},
    'Australia': {'Refugee population': 1770000},
    'South Africa': {'Refugee population': 280000},
    'Turkey': {'Refugee population': 3600000},
    'France': {'Refugee population': 130000},
    'Spain': {'Refugee population': 120000},
    'Sweden': {'Refugee population': 100000},
    'Norway': {'Refugee population': 90000},
    'Finland': {'Refugee population': 80000},
    'Italy': {'Refugee population': 70000},
    'New Zealand': {'Refugee population': 60000},
    'United Kingdom':{'Refugee population': 60000},
    'Hungary':{'Refugee population': 20000},
    'Portugal':{'Refugee population': 20000},
    'Ireland':{'Refugee population': 20000},
    'Czech Republic':{'Refugee population': 20000},
    'Denmark':{'Refugee population': 10000},
    'Netherlands':{'Refugee population': 10000},
    'Belgium':{'Refugee population': 10000}
}

world_map = folium.Map(location=map_center, zoom_start=zoom_start)

# Add markers for the original top ten countries
for country_name in ['Iran', 'Ethiopia', 'Bangladesh', 'Sudan', 'Poland', 'Russia', 'Uganda', 'Pakistan', 'Germany', 'Turkey']:
    refugee_info = refugee_data[country_name]
    refugee_str = f"Number of DISPLACED refugees after shift: {refugee_info['Refugee population']:,}"
    # f"Government spending on refugees: ${spending_info['Refugee spending']:,}\nGovernment spending on foreign affairs: ${spending_info['Foreign affairs spending']:,}"
    popup_content = f"<b>{country_name}</b><br>{refugee_str}"
    marker = folium.Marker(location=[0, 0], popup=popup_content,icon=folium.Icon(color='lightgreen'))
    try:
        marker.location = [spending_data[country_name]['Latitude'], spending_data[country_name]['Longitude']]
    except KeyError:
        print(f"No coordinates found for {country_name}")
    marker.add_to(world_map)

# Add markers for the new countries with redistributed refugees
for country_name in ['Canada', 'Australia', 'South Africa', 'Turkey', 'France', 'Spain', 'Sweden', 'Norway', 'Finland', 'Italy', 'New Zealand', 'United Kingdom', 'Hungary', 'Portugal', 'Ireland', 'Czech Republic', 'Denmark', 'Netherlands', 'Belgium']:
    refugee_info = refugee_data_redistributed[country_name]
    refugee_str = f"Number of NEW refugees: {refugee_info['Refugee population']:,}"
    popup_content = f"<b>{country_name}</b><br>{refugee_str}"
    marker = folium.Marker(location=[0, 0], popup=popup_content,icon=folium.Icon(color='darkgreen'))
    try:
        marker.location = [spending_data[country_name]['Latitude'], spending_data[country_name]['Longitude']]
    except KeyError:
        print(f"No coordinates found for {country_name}")
    marker.add_to(world_map)

'---------------------------------------------------------------------------------------------------------'

def get_popup_content(country_name):
    
    if country_name in spending_data:
        spending_info = spending_data[country_name]
        
        spending_str = f"Government spending on refugees: ${spending_info['Refugee spending']:,}\nGovernment spending on foreign affairs: ${spending_info['Foreign affairs spending']:,}"
    else:
        spending_str = "No data available on government spending"
    
    
    if country_name in refugee_data:
        refugee_info = refugee_data[country_name]
        
        refugee_str = f"Number of displaced refugees: {refugee_info['Refugee population']:,}"
    else:
        refugee_str = "No data available on refugee population"
    
    
    popup_content = f"<b>{country_name}</b><br>{spending_str}<br>{refugee_str}"
    return popup_content

for country_name in ['India', 'United States', 'Brazil', 'China', 'Indonesia', 'Nigeria', 'Japan', 'Mexico', 'South Korea', 'Argentina', 'Ukraine', 'Colombia', 'Saudi Arabia', 'Egypt', 'Peru', 'Iraq', 'Philippines', 'Thailand', 'Israel', 'Greece', 'Romania', 'Singapore', 'Malaysia', 'Venezuela', 'Chile', 'Kazakhstan', 'Morocco', 'Algeria', 'Vietnam', 'Tanzania', 'Kenya', 'Angola', 'Ghana', 'Zimbabwe', 'Tunisia', 'Jordan', 'Lebanon']:
    popup_content = get_popup_content(country_name)
    marker = folium.Marker(location=[0,0], popup=popup_content)
    try:
        marker.location = [spending_data[country_name]['Latitude'], spending_data[country_name]['Longitude']]
    except KeyError:
        print(f"No coordinates found for {country_name}")
    marker.add_to(world_map)

coords = [30,0]
map_obj = Map(center=coords, zoom_start=zoom_start)
map_obj.showMap(world_map)