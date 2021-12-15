from control.matlab import tf, c2d, feedback, stepinfo, step, lsim
import math
import matplotlib.pyplot as plt
import numpy as np

s = tf('s')
z = tf('z')

k = 2
tp = 1
T = 0.01

Wn = (s + 12) / ((s - 5)*(s + 8))

R = ((s + 8) * ((3 / math.pow(6.2, 2) + 5 / math.pow(6.2, 3)) * (s * s) + (3 / 6.2) * s + 1)) / ((s + 12) * s * s * 1 / math.pow(6.2, 3))


Wn_dis = c2d(Wn, T)
R_dis = c2d(R, T)

Wyg_dis = feedback(R_dis * Wn_dis, 1, -1)


#Единичное ступ. воздействие
h, T_step = step(Wyg_dis, 2)

info = stepinfo(Wyg_dis, SettlingTimeThreshold=0.05)

print('SettlingTime: %.4f' % (info['SettlingTime']))
plt.step(T_step, h)
plt.xlabel('t')
plt.ylabel('h step')
plt.title('h[lT], g[lT] = 1')
plt.show()

# Ошибка step
Weg = feedback(1, R_dis * Wn_dis, -1)

e_g, T_e = step(Weg, 2)

plt.step(T_e, e_g)
plt.xlabel('t')
plt.ylabel('e_g step')
plt.title('e[lt], g[lt] = 1')
plt.show()


# Ошибка lsim
t = np.arange(0, 1.1, 0.1)
g = 2*t + 1

e_g_lsim = lsim(Weg, g, t)
e_g_yout = e_g_lsim[0]
e_g_time = e_g_lsim[1]
plt.step(e_g_time, e_g_yout)
plt.xlabel('t')
plt.ylabel('e_g lsim')
plt.title('e[lT]; g[lT] = 2lT + 1')
plt.show()

