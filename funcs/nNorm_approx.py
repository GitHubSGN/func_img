import numpy as np
from tools.draw_util import line_plot
from scipy.stats import norm

def nNorm_approx():
    '''
    y = ln(1 + x^2)
    :return:
    '''
    mean = 0
    std_dev = 1

    x = np.arange(-2000,2000) / 1000
    # 使用norm.cdf计算标准正态分布的累积分布函数值
    cdf_value = norm.cdf(x, loc=mean, scale=std_dev)

    # Kendall &. Stuart
    cdf_approx = 0.5 + 1 / np.sqrt(2*np.pi) * (x - np.power(x,3) / 5)

    line_plot(list(x), [list(cdf_value), list(cdf_approx)], legend=["N", "N_approx"], x_label='x', y_label='y',
              figure_name=f'N = cdf of Norm dis. &. N_approx ')

if __name__ == '__main__':
    nNorm_approx()
