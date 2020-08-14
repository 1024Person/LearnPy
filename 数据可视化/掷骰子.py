# # # -*- coding: utf-8 -*-
# #
# # # !/usr/bin/env python
# #
# # import numpy as np
# #
# # import matplotlib.pyplot as plt
# #
# # x = [0, 1, 2, 4, 5, 6]
# #
# # y = [1, 2, 3, 2, 4, 1]
# #
# # z = [1, 2, 3, 4, 5, 6]
# #
# # plt.plot(x, y, '-*r', x, z, '-.+g')
# #
# # plt.xlabel("x-axis")
# #
# # plt.ylabel("y-axis")
# #
# # plt.title("hello world")
# #
# # plt.show()
#
#
# # -*- coding: utf-8 -*-
#
# # !/usr/bin/env python
#
# import numpy as np
#
# import matplotlib.pyplot as plt
#
# x = [0, 1, 2, 4, 5, 6]
#
# y = [1, 2, 3, 2, 4, 1]
#
# z = [1, 2, 3, 4, 5, 6]
#
# plt.figure('一')
#
# plt.subplot(2, 1, 1)
#
# plt.plot(x, y, '-+b')
#
# plt.subplot(2, 1, 2)
#
# plt.plot(x, z, '--*r')
# # --是虚线的意思，-是实线的意思，*和+都是拐点处的标志
#
# plt.show()
# -*- Author: JH -*-
import json
from pygal_maps_world.i18n import COUNTRIES
import pygal
from pygal.style import LightColorizedStyle as LCS, RotateStyle as RS
def get_country_code(country_name):
    """定义一个获取国别码的函数 """
    for code, name in COUNTRIES.items():
        # 只获取指定国家的国别码
        if name == country_name:
            return code
    return None
# 读取世界人数数据集中的人口数据
filename = "population_data.json"
with open(filename) as f:
    pop_data = json.load(f)
# 创建一个存储国别码：人口的列表
dir_population = {}
for pop_dict in pop_data:
    # 读取其中2010年人口数据
    if pop_dict["Year"] == "2010":
        country_name = pop_dict["Country Name"]
        population = int(float(pop_dict["Value"]))
        code = get_country_code(country_name)
        if code:
            dir_population[code] = population
# 绘制世界人口地图
wm_style = RS('#990000', base_style=LCS) # 加亮颜色主题
wm = pygal.maps.world.World(style=wm_style)
wm.title = "Global Population in 2010 by Country"
wm.add("2010", dir_population)
wm.render_to_file("Global_Population.svg")