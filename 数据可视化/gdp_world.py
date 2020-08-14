import pygal
import json
from countres import get_country_code
from pygal.style import RotateStyle as RS, \
    LightColorizedStyle as LCS

filename = 'gdp_json.json'
gdp_dict = {}
with open(filename) as f:
    gdp = json.load(f)
    # 将国家的gdp读取到程序中
    for cg in gdp:  # 国家gdp
        if cg['Year'] == 2015:
            code = get_country_code(cg['Country Name'])
            if code:
                val = int(float(cg['Value']))
                gdp_dict[code] = val
print(gdp_dict)
gdp_dict1, gdp_dict2, gdp_dict3 = {}, {}, {}
for c, v in gdp_dict.items():
    if v > 10 ** 13:
        gdp_dict1[c] = v
    elif v > 10 ** 10:
        gdp_dict2[c] = v
    else:
        gdp_dict3[c] = v

gwm_style = RS('#336699', base_style=LCS)
gwm = pygal.maps.world.World(style=gwm_style)
gwm.add('>10e + 13',gdp_dict1)
gwm.add('>10e+10',gdp_dict2)
gwm.add('>0',gdp_dict3)

gwm.render_to_file('2015_GDP.svg')
