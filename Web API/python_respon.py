from function import get_my_figure as gf, \
    get_dict_list as gdl_n, \
    drew_chart as dc

dicts_list, names = gdl_n()  # 获取字典列表和姓名列表

my_figure = gf(names)  # 获取配置信息

dc(my_figure, dicts_list, 'Python Repositories.svg')  # 绘画柱状图
