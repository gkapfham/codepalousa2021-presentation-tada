import matplotlib
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np

font = {'family' : 'sans-serif',
        'weight' : 'normal',
        'size'   : 18}

matplotlib.rc('font', **font)

fig = plt.figure()
ax = plt.axes()
ax.set_aspect('equal')

x = np.linspace(0, 10, 1000)

plt.figure(figsize=(16,9))

plt.title("Order of Growth Functions")
plt.xlabel("x")
plt.ylabel("f(x)")

# xmin, xmax, ymin, ymax
plt.axis([1, 10, 1, 1000]);

plt.plot(x, np.log2(x), linestyle='solid', label="f(x)=$log_2(x)$")
plt.plot(x, x, linestyle='solid', label="f(x)=x")
plt.plot(x, 2 * x + 10, linestyle='solid', label="f(x)=2x+10")
plt.plot(x, x * x, linestyle='dashed', label="f(x) = $x^2$")
plt.plot(x, x * x * x, linestyle='dashdot', label="f(x) = $x^3$")
plt.plot(x, np.exp2(x), linestyle='dotted', label="f(x) = $2^x$");
plt.legend();

# plt_1 = plt.figure(figsize=(6, 3))

plt.savefig('functions.png', transparent=True, dpi=300)
plt.savefig('functions.pdf')
