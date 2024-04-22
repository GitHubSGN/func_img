import numpy as np
from tools.draw_util import line_plot

def ln_1plusx():
    '''
    y = ln(1 + x^2)
    :return:
    '''

    x = np.arange(-999,999) / 1000
    y1 = np.log( 1 + x )
    y2 = np.zeros_like(x)
    order_num = 30   # 100
    for i in range(order_num):
        y2 = y2 + np.power(x, i+1) / (i+1) * (1 if i % 2==0 else -1)

    line_plot(list(x), [list(y1), list(y2)], legend=["y1", "y2"], x_label='x', y_label='y',
              figure_name=f'y1 = Ln(1 + x) &. y2 = TSE of y1')

if __name__ == '__main__':
    ln_1plusx()
