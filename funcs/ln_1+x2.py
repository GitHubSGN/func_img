import numpy as np
from tools.draw_util import line_plot

def ln_1plusx2():
    '''
    y = ln(1 + x^2)
    :return:
    '''

    x = np.arange(-5000,5000) / 1000
    y1 = np.log( 1 + np.power(x,2) )
    y2 = 2 * x / (1 + np.power(x,2))

    line_plot(list(x), [list(y1), list(y2)], legend=["y1", "y2"], x_label='x', y_label='y',
              figure_name=f'y1 = Ln(1 + x^2) &. y2 = 2x/(1+x^2)')

if __name__ == '__main__':
    ln_1plusx2()
