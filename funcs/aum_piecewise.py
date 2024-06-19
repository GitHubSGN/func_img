import numpy as np
from tools.draw_util import line_plot

def aum_piecewise():
    '''
    aum_piecewise
    '''

    AUM = 10 * 1e6

    x = np.arange(1,999) * 1e6 / 100 * 3
    # y := round(min(max(AUM/x * 0.15, 0.1), 0.25) / 0.05) * 0.05
    y = AUM / x * 0.15
    y[y<0.1] = 0.1
    y[y>0.25] = 0.25
    y = (y / 0.05).round() * 0.05


    line_plot(list(x), [list(y)], legend=["AUM Constraint"], x_label='AUM', y_label='constraint',
              figure_name=f'AUM Constraint v.s. AUM', file_name="aum_piecewise.png")

if __name__ == '__main__':
    aum_piecewise()