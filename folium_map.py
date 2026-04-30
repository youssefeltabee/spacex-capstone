#!/usr/bin/env python3
"""Generate interactive Folium map with SpaceX launch sites from dataset_part_2.csv."""
import pandas as pd
import folium
from folium.plugins import MarkerCluster

def main():
    # Load dataset
    df = pd.read_csv('dataset_part_2.csv')
    # Coordinates for launch sites
    site_coords = {
        'CCAFS SLC 40': (28.5618571, -80.577366),
        'KSC LC 39A': (28.6080585, -80.6039558),
        'VAFB SLC 4E': (34.632093, -120.610829),
    }
    # Color mapping
    def marker_color(cls):
        return 'green' if str(cls).strip() == '1' else 'red'
    
    # Create base map
    m = folium.Map(location=[30, -100], zoom_start=4, tiles='OpenStreetMap')
    cluster = MarkerCluster().add_to(m)
    
    for _, row in df.iterrows():
        site = row['LaunchSite']
        coords = site_coords.get(site)
        if not coords:
            continue
        cls = str(row['Class']).strip()
        color = marker_color(cls)
        outcome = 'Success' if cls == '1' else 'Failure'
        folium.CircleMarker(
            location=coords,
            radius=6,
            popup=f"Site: {site}<br>Orbit: {row['Orbit']}<br>Outcome: {outcome}<br>Payload: {row['PayloadMass']} kg",
            color=color,
            fill=True,
            fill_color=color,
            fill_opacity=0.7
        ).add_to(cluster)
    
    # Add site markers with labels
    for site, coords in site_coords.items():
        folium.Marker(
            location=coords,
            popup=site,
            icon=folium.Icon(color='blue', icon='info-sign')
        ).add_to(m)
    
    # Save
    out = 'spacex_launch_map.html'
    m.save(out)
    print(f'Folium interactive map saved to {out}')

if __name__ == '__main__':
    main()
