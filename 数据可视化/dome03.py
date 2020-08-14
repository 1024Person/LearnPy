# 随机漫步

import matplotlib.pyplot as plt
from RandWalk import RandomWalk

r = RandomWalk()
print(len(r.x))
r.fill_walk()
plt.title('RandomWalk', fontsize=24)

plt.xlabel('x', fontsize=15, c='blue')
plt.ylabel('y', fontsize=15, c='blue')
plt.scatter(r.x, r.y, s=10, c=r.y, cmap=plt.cm.Reds)

plt.savefig('随机漫步生成图.png', bbox_chaes='tight')

# plt.show()
