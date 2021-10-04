import json
from landsatxplore.api import API
from pprint import pprint
# Initialize a new API instance and get an access key
username = "batuhang"
password = "SLCH6i5k9L.."
api = API(username, password)

# Search for Landsat TM scenes
scenes = api.search(
    dataset='landsat_8_c1',
    latitude=28.85,
    longitude=41.35,
    start_date='2019-01-01',
    end_date='2021-10-01',
    max_cloud_cover=50,
    min_cloud_cover=20
)

print(f"{len(scenes)} scenes found.")

# Process the result
for scene in scenes:
    # print(scene['acquisition_date'].strftime('%Y-%m-%d'))
    # # Write scene footprints to disk
    # fname = f"{scene['landsat_product_id']}.geojson"
    # with open(fname, "w") as f:
    #     json.dump(scene['spatial_coverage'].__geo_interface__, f)
    pprint(scene['entity_id'])

api.logout()

from landsatxplore.earthexplorer import EarthExplorer

ee = EarthExplorer(username, password)

ee.download(scenes[0]['entity_id'], output_dir='./data')