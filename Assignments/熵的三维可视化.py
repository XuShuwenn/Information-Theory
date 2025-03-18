import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x = np.linspace(0, 1, 100)  
y = np.linspace(0, 1, 100)  
x, y = np.meshgrid(x, y)  

# 定义熵函数
z = -(x*np.log(x)/np.log(2)+y*np.log(y)/np.log(2)+(1-x-y)*(np.log(1-x-y)/np.log(2)))

# 创建三维图形
fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111, projection='3d')

# 绘制三维曲面
ax.plot_surface(x, y, z, cmap='viridis')  # 使用 'viridis' 色图

# 添加标签
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
ax.grid(True)
plt.show()