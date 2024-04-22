import numpy as np
from tools.draw_util import line_plot

def e_neg_x2_half():
    '''
    y = exp(-x^2/2)
    :return:
    '''

    x = np.arange(-5000,5000) / 1000
    y = np.exp( -np.power(x,2) / 2 )

    line_plot(list(x), [list(y)], legend=None, x_label='x', y_label='y',
              figure_name=f'y = exp(-x^2/2)')

if __name__ == '__main__':
    e_neg_x2_half()
