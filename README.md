# ML_first_route
基于普通最小二乘法的）简单线性回归 -> 线性回归中的新进展（岭回归和LASSO回归）->(此处可以插入Bagging和AdaBoost的内容)-> Logistic回归 ->支持向量机（SVM）->感知机学习 -> 神经网络（初学者可先主要关注BP算法）-> 深度学习
注释：之所以把它们归为一条线路，因为所有这些算法都是围绕着 y = Σxiβi，这样一条简单的公式展开的，如果你抓住这条线索，不断探索下去，就算是抓住它们之间的绳索了。前半部分主要是回归，Logistic后面部分主要是有监督的分类学习法。基于普通最小二乘的线性回归是统计中一种有着非常悠久历史的方法，它的使用甚至可以追溯到高斯的时代。但是它对数据有诸多要求，例如特征之间不能有多重共线性，而且岭回归和LASSO就是对这些问题的修正。当沿着第一条路线学完的时候，其实你已经攻克机器学习的半壁江山了！当然，在这个过程中，你一定时刻问问自己后一个算法与前一个的联系在哪里?最初，人们从哪里出发，才会如此设计出它们的。