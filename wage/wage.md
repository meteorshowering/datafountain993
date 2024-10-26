### 相对合理的插值结果：
wage_linear.csv，根据空值位置前后取平均

wage_polynomaial_predicted.csv，根据已知点作多项式回归，预测空值（感觉这个图像画出来最合理）
### 不合理的插值结果
wage_cubicspline.csv 为样条插值结果，有剧烈下降

wage_lagrange.csv  为拉格朗日插值结果，效果最差，有负数

wage_linear_predicted.csv为线性回归结果，预测值通常和前一个值有明显下降，不太符合此前趋势

（虽然这些都不怎么合理，但还是传上来了，万一有用呢 （好吧其实没可能