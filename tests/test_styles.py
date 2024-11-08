import matplotlib.pyplot as plt


def simple_plot(title: str | None = None):
    fig, ax = plt.subplots()

    ax.set(title=title)
    ax.plot([0, 1, 2, 3], [0, 1, -1, 2])

    return fig, ax
    

def test_default_style():
    plt.style.use('mpl_utils.styles.default')

    assert plt.rcParams['axes.grid'] is True
    assert plt.rcParams['grid.linestyle'] == ':'


def test_default_style_plots():
    plt.style.use('mpl_utils.styles.default')

    fig, _ = simple_plot('Style "mpl_utils.styles.default" • Simple Plot')
    fig.savefig('tests/out/default_simple_plot.png')

