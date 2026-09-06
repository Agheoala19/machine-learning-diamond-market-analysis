import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd
from shapely.geometry import Point

def display_geo_analysis():
    # Centrele logistice și comerciale globale de diamante
    hubs_data = {
        'City': ['Antwerp', 'Mumbai', 'New York', 'Dubai', 'Tel Aviv', 'Gaborone'],
        'Country': ['Belgium', 'India', 'USA', 'UAE', 'Israel', 'Botswana'],
        'Latitude': [51.2194, 19.0760, 40.7128, 25.2048, 32.0853, -24.6282],
        'Longitude': [4.4025, 72.8777, -74.0060, 55.2708, 34.7818, 25.9231],
        'Market_Share_Pct': [35, 25, 15, 12, 8, 5]
    }

    df_hubs = pd.DataFrame(hubs_data)

    # Creare GeoDataFrame folosind Shapely Point
    geometry = [Point(xy) for xy in zip(df_hubs['Longitude'], df_hubs['Latitude'])]
    geo_df = gpd.GeoDataFrame(df_hubs, geometry=geometry, crs="EPSG:4346")

    # Generare hartă
    fig, ax = plt.subplots(figsize=(12, 6))
    
    # Harta de fundal a lumii
    world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
    world.plot(ax=ax, color='#e0e0e0', edgecolor='#ffffff')

    # Reprezentarea punctelor logistice proporțional cu importanța comercială
    geo_df.plot(
        ax=ax,
        markersize=geo_df['Market_Share_Pct'] * 15,
        color='#d90429',
        alpha=0.7,
        edgecolor='black'
    )

    # Etichete pentru fiecare hub
    for _, row in geo_df.iterrows():
        ax.annotate(
            text=f"{row['City']} ({row['Market_Share_Pct']}%)",
            xy=(row['Longitude'], row['Latitude']),
            xytext=(4, 4),
            textcoords="offset points",
            fontsize=9,
            fontweight='bold',
            color='#1a1a1a'
        )

    ax.set_title("Distribuția Principalelor Hub-uri Comerciale și Logistice de Diamante", fontsize=13, pad=12)
    ax.set_axis_off()
    fig.tight_layout()

    return fig
