import yaml
from yaml.loader import SafeLoader
from Instagram import Instagram
with open('resources/config.yaml') as conf:
    config = yaml.load(conf, Loader=SafeLoader)
    

inst = Instagram(config["client_id"],config["client_secret"],config["redirect_uri"])
code = "AQCQLDGFobkVdRpYAlDfCJKGIm62IuwC-W8woUJ6rrLrWyYVC-qVZqEXGHK_97cxLlRewU6oJxj-a0tNT6tiTs2dUL0hx_BLDtBqexRsDVOpHWHfSxn7eX1jz4Q2vowPX8JxN4SkGQuXOhaw3yLvk3OV03e9COjczOccNCW2_AkXplS0p68eDMzaEaSj9pc5l5ZIrHNaiCSbiE_dgjxipDXjDwOcOeF_TQ1G7_PWDRwiuA"

print(inst.get_short_lived_token(code= code))








