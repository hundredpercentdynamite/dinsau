from control.matlab import tf, c2d, feedback, stepinfo, step, lsim
import math
import matplotlib.pyplot as plt

s = tf('s')
k = 2
tp = 1
T = 0.01

Wn = (s + 12) / ((s - 5)*(s + 8))

R = ((s + 8) * ((3 / math.pow(6.2, 2) + 5 / math.pow(6.2, 3)) * (s * s) + (3 / 6.2) * s + 1)) / ((s + 12) * s * s * 1 / math.pow(6.2, 3))


Wn_dis = c2d(Wn, T)
R_dis = c2d(R, T)


Wyg_dis = feedback(R_dis * Wn_dis, 1, -1)


#Единичное ступ. воздействие
yout, T_step = step(Wyg_dis)

info = stepinfo(Wyg_dis, SettlingTimeThreshold=0.05)

print('SettlingTime:', info['SettlingTime'])
plt.plot(T_step, yout)
plt.xlabel('t')
plt.ylabel('yout')
plt.show()

# Ошибка ???????????????
Weg = feedback(1, R_dis * Wn_dis, -1)

e_g, T_e = step(Weg)

plt.plot(T_e, e_g)
plt.xlabel('t')
plt.ylabel('e_g')
plt.show()

