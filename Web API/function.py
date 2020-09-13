import pygal
from pygal.style import RotateStyle as RS, \
    LightColorizedStyle as LCS
import json


def get_my_figure(names):
    my_figure = pygal.Config()
    my_figure.style = RS('#114477', base_style=LCS)
    my_figure.show_legend = False
    my_figure.x_label_rotation = 45
    my_figure.title = 'Most stars Python projects of github '
    my_figure.x_labels = names
    my_figure.show_y_guides = False
    my_figure.width = 1000
    my_figure.x_title = 'Name'
    my_figure.y_title = 'Stars Count'
    my_figure.label_font_size = 14
    my_figure.title_font_size = 24
    return my_figure


def get_dict_list():
    """

    :return:返回字典列表
    """
    # 打开json文件
    PATH = 'repositories.json'
    with open(PATH, 'rb') as stream:
        response_dict = json.load(stream)
    # 得到仓库列表
    repositories_list = response_dict['items']
    names, plot_dicts_list = [], []
    for repo_dict in repositories_list:
        names.append(repo_dict['name'])

        plot_dict = {'value': repo_dict['stargazers_count'],
                     'label': str(repo_dict['description']),
                     'xlink': repo_dict['html_url'], }
        plot_dicts_list.append(plot_dict)

    return plot_dicts_list, names


def drew_chart(my_figure, dicts_list, filename):
    chart = pygal.Bar(my_figure)
    chart.add('', dicts_list)

    chart.render_to_file(filename)


if __name__ == '__main__':
    repositories_dict_list, names = get_dict_list()
    my_figure = get_my_figure(names)
    print(repositories_dict_list)
    drew_chart(my_figure, repositories_dict_list, 'python_respon.svg')
