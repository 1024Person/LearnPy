import pygal
import csv
from countres import get_country_code
from pygal.style import RotateStyle as RS, \
    LightColorizedStyle as LCS

filename = 'API_AG.LND.AGRI.ZS_DS2_en_csv_v2_1217657.csv'

country_dict = {}
with open(filename, encoding='utf-8') as f:
    data = csv.reader(f)
    for i in range(5):
        next(data)  # 先将没用的文件头读出来并且丢掉

    for country in data:
        try:
            country_name = country[0]
            country_code = get_country_code(country_name)
            land_rate = float(country[5])  # 1960年的数据
            if country_code:
                country_dict[country_code] = land_rate / 100
        except Exception as r:  # 有些数据不全，所以会出现异常的情况
            pass
cl_dict1, cl_dict2 = {}, {}
for c, v in country_dict.items():
    if v > 0.5:
        cl_dict1[c] = v
    else:
        cl_dict2[c] = v
wm_style = RS('#225588', base_style=LCS)
wm = pygal.maps.world.World(style=wm_style)
wm.add('<50%',cl_dict2)
wm.add('>50%', cl_dict1)

wm.render_to_file('land.svg')
