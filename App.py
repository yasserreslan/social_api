import yaml
from yaml.loader import SafeLoader
from Instagram import Instagram
with open('resources/config.yaml') as conf:
    config = yaml.load(conf, Loader=SafeLoader)
    

inst = Instagram(config["client_id"],config["client_secret"],config["redirect_uri"],v="v14.0")
code = "AQCQLDGFobkVdRpYAlDfCJKGIm62IuwC-W8woUJ6rrLrWyYVC-qVZqEXGHK_97cxLlRewU6oJxj-a0tNT6tiTs2dUL0hx_BLDtBqexRsDVOpHWHfSxn7eX1jz4Q2vowPX8JxN4SkGQuXOhaw3yLvk3OV03e9COjczOccNCW2_AkXplS0p68eDMzaEaSj9pc5l5ZIrHNaiCSbiE_dgjxipDXjDwOcOeF_TQ1G7_PWDRwiuA"

token = "IGQVJXOUVTVG9rbHlIYTh6MUxGVFdUWklqUVlBSW0zZA2xyaVhnYk4wSzJlc204UjU5RnpaeWw4TGNxOHA0by1XUHM5RXRkZAFc3QkdlQ2toTWkwZAEsyWGcyLWQwTE02ODI1aHFidkZAR"
print(inst.get_user_media(5877979025552411,token=token))








