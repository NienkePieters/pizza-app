from viktor import ViktorController
import matplotlib.pyplot as plt
import numpy as np
from io import StringIO
from viktor.views import SVGView, SVGResult
from viktor.parametrization import ViktorParametrization, IntegerField

class Controller(ViktorController):
    label = "My pizza"

    @SVGView("Pizza", duration_guess=1)
    def create_svg_result(self, params, **kwargs):

        #slices
        x1,y1 = [0, 1], [0.5,0.5]
        x2,y2 = [0.5, 0.5], [0, 1]

        #pizza base
        circle1 = plt.Circle((0.5, 0.5), 0.5, color='peru')
        circle2 = plt.Circle((0.5, 0.5), 0.4, color='wheat')

        #topping1
        r2 = 0.4 * np.sqrt(np.random.rand(10, 1))
        theta1 = 2 * np.pi * np.random.rand(10, 1)
        x3 = (r2 * np.cos(theta1))+0.5
        y3 = (r2 * np.sin(theta1))+0.5

        #topping2
        r3 = 0.4 * np.sqrt(np.random.rand(12, 1))
        theta2 = 2 * np.pi * np.random.rand(12, 1)
        x4 = (r3 * np.cos(theta2))+0.5
        y4 = (r3 * np.sin(theta2))+0.5

        #create plot
        fig, ax = plt.subplots() 

        ax.add_patch(circle1)
        ax.add_patch(circle2)

        
        plt.plot(x4,y4,'r.', markersize = 50)
        plt.plot(x3,y3,'g.', markersize = 40)

        plt.plot(x1,y1,x2,y2, color='w')

        plt.axis("equal")

        # save figure
        svg_data = StringIO()
        fig.savefig(svg_data, format = 'svg')
        plt.close()

        return SVGResult(svg_data)
