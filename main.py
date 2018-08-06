import matplotlib.pyplot as plt
from matplotlib import style
from scipy import stats
import numpy as np


def print_analysis(x, y):
    print('r = {}\nR² = {}\nstd. error: {}\np = {}'.format(r_value, r_value ** 2, std_err, p_value))

    sse = 0
    sst = 0
    for i, value in enumerate(x):
        y_predicted = value * slope + intercept
        residual = y[i] - y_predicted
        sse += residual ** 2
        sst += (y[i] - np.mean(y)) ** 2

    print('\nExplained Sum of Squares: {}\n'
          'Residual Sum of Squares: {}\n'
          'Total Sum of Squares: {}'.format(sst - sse, sse, sst))
    # print('R² = {}'.format(1 - sse/sst))

    return


def gen_confidence_bands(alpha, x, y):
    tot = 0
    for i, value in enumerate(x):
        y_predicted = value * slope + intercept
        tot += (y[i] - y_predicted) ** 2
    std_err_estimate = (tot / (len(y) - 2)) ** (1/2)

    x_band_points = []
    y_upper_band = []
    y_lower_band = []
    x_step = 0.1

    t_critical = stats.t.ppf(1 - alpha / 2, len(x) - 2)

    denominator = 0
    for item in x:
        denominator += (item - np.mean(x)) ** 2

    for item in np.arange(min(x), max(x) + x_step, x_step):
        x_band_points.append(item)
        s_y_star = std_err_estimate * (1 / len(x) + (item - np.mean(x)) ** 2 / denominator) ** (1/2)
        y_predicted = item * slope + intercept
        y_upper_band.append(y_predicted + t_critical * s_y_star)
        y_lower_band.append(y_predicted - t_critical * s_y_star)

    return x_band_points, y_lower_band, y_upper_band


def plot_data():
    black = '#0F0F0F'
    bg_color = '#F1F1F1'
    point_color = '#AA00AA'

    style.use('ggplot')
    fig = plt.figure()
    ax1 = plt.subplot2grid((1, 1), (0, 0))
    fig.set_facecolor(bg_color)
    fig.set_size_inches(12, 6.5)
    fig.subplots_adjust(bottom=0.16)

    plt.scatter(recruit_avg, s_and_p, color=point_color)

    plt.plot([min(recruit_avg), max(recruit_avg)],
             [min(recruit_avg) * slope + intercept, max(recruit_avg) * slope + intercept],
             linestyle='--', color=black)

    ax1.fill_between(confidence_band_points, lower_band, upper_band, color=black, alpha=0.30)

    plt.xticks(np.arange(10, 110, 10))
    ax1.tick_params(labelsize=13)

    title_font = {'fontname': 'Ubuntu', 'fontsize': '22', 'weight': 'bold'}
    axis_label_font = {'fontname': 'Ubuntu', 'fontsize': '15'}

    plt.title('College Football Recruiting vs. S&P+ Rating [2007-2017]', title_font)
    plt.xlabel('Avg. Recruiting Percentile Over Prev. 4 Years', axis_label_font, labelpad=20)
    plt.ylabel('Final S&P+ Rating', axis_label_font, labelpad=20)

    data_summary = 'n = {}\nR² = {}'.format(len(team), round(r_value ** 2, 4))
    ax1.text(90, 24, data_summary, {'fontname': 'Ubuntu', 'fontsize': '12', 'weight': 'bold'},
             bbox={'boxstyle': 'round', 'facecolor': 'wheat', 'edgecolor': '#000000',
                   'linewidth': '2', 'alpha': 0.6, 'pad': 0.5})

    plt.show()

    return


season, team, recruit_avg, s_and_p = np.genfromtxt('recruit_sp_data.csv', delimiter=',', unpack=True)

slope, intercept, r_value, p_value, std_err = stats.linregress(recruit_avg, s_and_p)

print_analysis(x=recruit_avg, y=s_and_p)

confidence_band_points, lower_band, upper_band = gen_confidence_bands(alpha=0.05, x=recruit_avg, y=s_and_p)

plot_data()
