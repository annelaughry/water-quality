import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

file_path = 'file path here'
df = pd.read_csv(file_path)


status_mapping = {
    "High": 1,
    "Acceptable": 0
}

columns_to_map = ['Lead', 'Copper', 'Iron', 'Nitrates', 'Nitrites'] 
for column in columns_to_map:
    df[column] = df[column].map(status_mapping)


def heavy_metals_status(row):
    if (row['Lead'] > 0 or
        row['Iron'] > 0 or
        row['Copper'] > 0):
        return 'red'
    return 'green'

def nutrients_status(row):
    if (row['Nitrates'] > 0 or
        row['Nitrites'] > 0):
        return 'red'
    return 'green'

# Apply the functions to create new columns for status
df['heavy_metals_status'] = df.apply(heavy_metals_status, axis=1)
df['nutrients_status'] = df.apply(nutrients_status, axis=1)

# Create maps
fig_heavy_metals = px.scatter_mapbox(
    df,
    lat='Latitude',
    lon='Longitude',
    color='heavy_metals_status',
    color_discrete_map={'green': 'green', 'red': 'red'},
    title="Heavy Metals Status",
    mapbox_style="open-street-map",
    zoom=10
)

fig_nutrients = px.scatter_mapbox(
    df,
    lat='Latitude',
    lon='Longitude',
    color='nutrients_status',
    color_discrete_map={'green': 'green', 'red': 'red'},
    title="Nutrients Status",
    mapbox_style="open-street-map",
    zoom=10
)

# Show maps
fig_heavy_metals.update_traces(marker=dict(size=15))
fig_nutrients.update_traces(marker=dict(size=15))
fig_heavy_metals.show()
fig_nutrients.show()