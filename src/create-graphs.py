import matplotlib
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np


def create_slow_growth_functions():
    font = {'family' : 'sans-serif',
            'weight' : 'normal',
            'size'   : 18}

    matplotlib.rc('font', **font)

    fig = plt.figure()
    ax = plt.axes()
    ax.set_aspect('equal')

    x = np.linspace(0, 10, 1000)

    plt.figure(figsize=(16,9))

    plt.xlabel("n")
    plt.ylabel("f(n)")

    # xmin, xmax, ymin, ymax
    plt.axis([1, 10, 1, 100]);

    plt.plot(x, np.log2(x), linestyle='solid', label="f(n)=$log_2(n)$")
    plt.plot(x, x * np.log2(x), linestyle='solid', label="f(n)=$n*log_2(n)$")
    plt.plot(x, x, linestyle='solid', label="f(n)=n")
    plt.plot(x, 2 * x + 10, linestyle='solid', label="f(n)=2n+10")
    plt.plot(x, x * x, linestyle='dashed', label="f(n) = $n^2$")
    plt.legend();

    plt.savefig('../public/slow-growth-functions.png', transparent=True, dpi=300)


def create_fast_growth_functions():
    font = {'family' : 'sans-serif',
            'weight' : 'normal',
            'size'   : 18}

    matplotlib.rc('font', **font)

    fig = plt.figure()
    ax = plt.axes()
    ax.set_aspect('equal')

    x = np.linspace(0, 10, 1000)

    plt.figure(figsize=(16,9))

    plt.xlabel("n")
    plt.ylabel("f(n)")

    # xmin, xmax, ymin, ymax
    plt.axis([1, 10, 1, 1000]);

    plt.plot(x, x * np.log2(x), linestyle='solid', label="f(n)=$n*log_2(n)$")
    plt.plot(x, x * x, linestyle='dashed', label="f(n) = $n^2$")
    plt.plot(x, x * x * x, linestyle='dashdot', label="f(n) = $n^3$")
    plt.plot(x, np.exp2(x), linestyle='dotted', label="f(n) = $2^n$");
    plt.legend();

    plt.savefig('../public/fast-growth-functions.png', transparent=True, dpi=300)


def create_all_functions():
    font = {'family' : 'sans-serif',
            'weight' : 'normal',
            'size'   : 18}

    matplotlib.rc('font', **font)

    fig = plt.figure()
    ax = plt.axes()
    ax.set_aspect('equal')

    x = np.linspace(0, 1, 1000)

    plt.figure(figsize=(16,9))

    plt.xlabel("n")
    plt.ylabel("f(n)")

    # xmin, xmax, ymin, ymax
    plt.axis([1, 10, 1, 1000]);

    plt.plot(x, np.log2(x), linestyle='solid', label="f(n)=$log_2(n)$")
    plt.plot(x, x * np.log2(x), linestyle='solid', label="f(n)=$n*log_2(n)$")
    plt.plot(x, x, linestyle='solid', label="f(n)=n")
    plt.plot(x, 2 * x + 10, linestyle='solid', label="f(n)=2n+10")
    plt.plot(x, x * x, linestyle='dashed', label="f(n) = $n^2$")
    plt.plot(x, x * x * x, linestyle='dashdot', label="f(n) = $n^3$")
    plt.plot(x, np.exp2(x), linestyle='dotted', label="f(n) = $2^n$");
    plt.legend();

    plt.savefig('../public/all-functions.png', transparent=True, dpi=300)

create_slow_growth_functions()
create_fast_growth_functions()
create_all_functions()
