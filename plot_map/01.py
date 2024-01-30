import plotly.express as px
import pandas as pd

import plotly.express as px
#df = px.data.gapminder().query("year == 2007")
#print (df)
df = pd.read_csv('data.txt', '\t')
print (df)
fig = px.scatter_geo(df,
                     #locations="iso_alpha",
                        lat=df.lat,
                        lon=df.long,
                     color=df.City, # which column to use to set the color of markers
                     hover_name=df.City, # column added to hover information
                     size="counts", # size of markers
                     projection="natural earth"
                     )
fig.show()

# #px.set_mapbox_access_token(open(".mapbox_token").read())
# df = pd.read_csv('data.txt', '\t')
#
# #df = px.data.carshare()
# fig = px.scatter_mapbox(df, lat="lat", lon="long",     color="counts", size="counts",
#                   color_continuous_scale=px.colors.cyclical.IceFire, zoom=10, center=dict( lat=8.584314, lon=-75.95781 ))
# #fig["layout"].pop("updatemenus")
# fig.update_layout(mapbox_style="carto-positron")
# fig.show()
# #fig.show()