#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import random

plt.figure(figsize=(15, 2))

n = 100 #X轴长度（最大显示人数）
x = list(range(n+1))
y = [0]*(n+1)
prob = 0.05 #原定概率
N = 1000000 #模拟抽卡次数
db = 0 #欧皇限制
tb = 60 #低保限制
print("原定概率：", prob, "模拟抽卡次数：", N, "欧皇限制：", db, "低保限制：", tb)
cut = min(tb, n) - 1

ct = 0
for i in range(N):
	ct += 1
	if ct >= db and (random.random() < prob or ct >= tb):
		if ct < n:
			y[ct] += 1
		ct = 0

x = x[1:]
y = y[1:]
print("真随机 最后抽到概率期望:", sum(y) / N, "低保线玩家占比：", y[cut]/sum(y))

plt.subplot(131)
plt.bar(x, y)

x = list(range(n+1))
y = [0]*(n+1)

C = 0.0038 #伪随机调整值，调整到最后期望与预期差不多即可
ct = 0
for i in range(N):
	ct += 1
	if ct >= db and (random.random() < ct * C or ct >= tb):
		if ct < n:
			y[ct] += 1
		ct = 0
x = x[1:]
y = y[1:]
print("伪随机 最后抽到概率期望:", sum(y) / N, "低保线玩家占比：", y[cut]/sum(y))

plt.subplot(132)
plt.bar(x, y)
plt.show()