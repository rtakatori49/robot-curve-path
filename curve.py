import numpy as np
import matplotlib.pyplot as plt

def de_casteljau(t, coefs):
    beta = [c for c in coefs] # values in this list are overridden
    n = len(beta)
    for j in range(1, n):
        for k in range(n - j):
            beta[k] = beta[k] * (1 - t) + beta[k + 1] * t
    return beta[0]

def get_curve(points, t_size):
    t_span = np.linspace(0, 1, t_size)
    curve = [[], []]
    temp = [[], []]
    for point in points:
        for x in range(2):
            temp[x].append(point[x])
    for x in range(2):
        curve[x] = [de_casteljau(t, temp[x]) for t in t_span]
    return curve

def vector_projection(point_given, theta_given):
    if 90 in theta_given:
        theta_90 = theta_given.index(90)
    else:
        theta_90 = None
    theta_given = [np.deg2rad(theta) for theta in theta_given]
    vector_given = [[np.cos(theta), np.sin(theta)] for theta in theta_given]
    slope = [np.tan(theta) for theta in theta_given]
    a = [[slope[0], -1],
        [slope[1], -1]]
    b = [[slope[0]*point_given[0][0]-point_given[0][1]],
        [slope[1]*point_given[1][0]-point_given[1][1]]]
    x = np.linalg.inv(a).dot(b)
    if theta_90 == 0:
        x[theta_90] = point_given[1][1]
    elif theta_90 == 1:
        x[theta_90] = point_given[0][1]
    return vector_given, x.T[0]

def main():
    t_size = 100
    point_given = [[70, 0], [0, 50]]
    theta_given = [110, 150]
    vector_given, point = vector_projection(point_given, theta_given)
    points = [point_given[0], point, point_given[1]]
    xy = []
    xytext = []
    # for x in range(2):
    #     if vector_given[x][0] > 0:
    #         value_x = vector_given[x][0]*point_given[x][0]*1.1
    #     else:
    #         value_x = abs(vector_given[x][0]*point_given[x][0]*0.9)
    #     if vector_given[x][1] > 0:
    #         value_y = vector_given[x][1]*point_given[x][1]*1.1
    #     else:
    #         value_y = abs(vector_given[x][1]*point_given[x][1]*0.9)
    #     value = (value_x, value_y)
    #     xy.append(value)
    #     xytext.append((point_given[x][0], point_given[x][1]))
    # print(xy)
    curve = get_curve(points, t_size)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(point_given[0][0], point_given[0][1], 'o')
    ax.plot(point_given[1][0], point_given[1][1], 'o')
    ax.plot(curve[0], curve[1])
    # ax.annotate('start', xy=xy[0],
    #          xycoords='data',
    #          annotation_clip=False,
    #          xytext=xytext[0],
    #          arrowprops=dict(arrowstyle= '->',
    #                          lw=3.5,
    #                          ls='-')
    #        )
    # ax.annotate('end', xy=xy[1],
    #          xycoords='data',
    #          xytext=xytext[1],
    #          annotation_clip=False,
    #          arrowprops=dict(arrowstyle= '->',
    #                          lw=3.5,
    #                          ls='-',
    #                          relpos=(0, 0))
    #        )
    plt.show()
    
if __name__ == '__main__':
    main()