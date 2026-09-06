import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd
from shapely.geometry import Point

def display_geo_analysis():
    hubs_data = {
        'City': ['Antwerp', 'Mumbai', 'New York', 'Dubai', 'Tel Aviv', 'Gaborone'],
        'Country': ['Belgium', 'India', 'USA', 'UAE', 'Israel', 'Botswana'],
        'Latitude': [51.2194, 19.0760, 40.7128, 25.2048, 32.0853, -24.6282],
        'Longitude': [4.4025, 72.8777, -74.0060, 55.2708, 34.7818, 25.9231],
        'Market_Share_Pct': [35, 25, 15, 12, 8, 5]
    }

    df_hubs = pd.DataFrame(hubs_data)
    geometry = [Point(xy) for xy in zip(df_hubs['Longitude'], df_hubs['Latitude'])]
    geo_df = gpd.GeoDataFrame(df_hubs, geometry=geometry, crs="EPSG:4326")

    fig, ax = plt.subplots(figsize=(12, 6))

    # Încărcare hartă a lumii via URL public stabil
    world_url = "https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master/geojson/ne_110m_admin_0_countries.geojson"
    try:
        world = gpd.read_file(world_url)
        world.plot(ax=ax, color='#e9ecef', edgecolor='#adb5bd')
    except Exception:
        # Fallback dacă rețeaua e blocată
        ax.set_facecolor('#f8f9fa')
        ax.grid(True, linestyle='--', alpha=0.5)

    # Plotare centre logistice
    geo_df.plot(
        ax=ax,
        markersize=geo_df['Market_Share_Pct'] * 25,
        color='#e63946',
        alpha=0.8,
        edgecolor='black'
    )

    for _, row in geo_df.iterrows():
        ax.annotate(
            text=f"{row['City']} ({row['Market_Share_Pct']}%)",
            xy=(row['Longitude'], row['Latitude']),
            xytext=(5, 5),
            textcoords="offset points",
            fontsize=9,
            fontweight='bold',
            color='#1d3557'
        )

    ax.set_title("Distribuția Principalelor Hub-uri Comerciale și Logistice de Diamante", fontsize=13, pad=12)
    ax.set_xlim(-180, 180)
    ax.set_ylim(-60, 85)
    ax.set_axis_off()
    fig.tight_layout()

    return fig
