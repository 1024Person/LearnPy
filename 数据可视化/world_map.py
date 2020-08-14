import json
import pygal
from pygal.style import LightColorizedStyle as LCS, \
    RotateStyle as RS

from countres import get_country_code

# 将数据读入到程序中
filename = 'population_data.json'
country_dict = {}
with open(filename) as rstream:
    reader = json.load(rstream)
    # for row in reader:
    #     if row['Year'] == '2010':
    #         country_name = row['Country Name']
    #         country_code = get_country_code(country_name)
    #         country_num = int(float(row['Value']))

    for country in reader:
        if country["Year"] == '2010':
            country_name = country["Country Name"]
            code = get_country_code(country_name)
            val = int(float(country['Value']))
            if code:
                country_dict[code] = val

cc_pop1, cc_pop2, cc_pop3 = {}, {}, {},
for cc, pop in country_dict.items():
    if pop < 10000000:
        cc_pop1[cc] = pop
    elif pop < 1000000000:
        cc_pop2[cc] = pop
    else:
        cc_pop3[cc] = pop

wm_style = RS('#225588', base_style=LCS)
wm = pygal.maps.world.World(style=wm_style)
wm.add('0-10m', cc_pop1)
wm.add('10m - 10bn', cc_pop2)
wm.add('>10bn', cc_pop3)
wm.render_to_file('World Map.svg')
