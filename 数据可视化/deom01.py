import matplotlib.pyplot as plt

s_output = [1, 4, 9, 16, 25]
s_input = [1, 2, 3, 4, 5]
plt.plot(s_input, s_output, linewidth=5)
# 参数位置：第一个是输入数据，第二个是输出数据，
# 第三个是指定线条宽度
plt.title('Square Numbers', fontsize=48)  # 标题
plt.xlabel('value', fontsize=10)  # 设置x轴的标题
plt.ylabel('Square of value', fontsize=10)  # 设置y轴的标题

plt.tick_params(axis='both', labelsize=10)  # 设置

plt.show()
