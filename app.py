from viktor import ViktorController
import matplotlib.pyplot as plt
import numpy as np
from io import StringIO
from viktor.views import SVGView, SVGResult
from viktor.parametrization import ViktorParametrization, MultiSelectField, Text, IntegerField 

class Parametrization(ViktorParametrization):
    text = Text("# Hi! Create your own pizza for VIKTOR's pizza night!")
    slices = IntegerField('How many slices?', default=0, step = 4, min=0, max=8)
    toppings = MultiSelectField('Which toppings?', options=['tomato', 'tuna', 'pineapple', 'spinach'], default=['tomato'])

class Controller(ViktorController):
    label = "My pizza"
    parametrization = Parametrization(width=20)

    @SVGView("Pizza", duration_guess=1)
    def create_svg_result(self, params, **kwargs):

        #create plot
        fig, ax = plt.subplots() 

        img = plt.imread("pizzabox.jpg")
        ax.imshow(img,extent=[-0.5,1.5,-0.5,1.5])

        #Create pizza base
        circle1 = plt.Circle((0.5, 0.5), 0.55, color='peru')
        circle2 = plt.Circle((0.5, 0.5), 0.45, color='wheat')

        ax.add_patch(circle1)
        ax.add_patch(circle2)    

        #Add the toppings

        #tuna
        r1 = 0.4 * np.sqrt(np.random.rand(12, 1))
        theta1 = 2 * np.pi * np.random.rand(12, 1)
        top_x1 = (r1 * np.cos(theta1))+0.5
        top_y1 = (r1 * np.sin(theta1))+0.5

        #tomato
        r2 = 0.4 * np.sqrt(np.random.rand(14, 1))
        theta2 = 2 * np.pi * np.random.rand(14, 1)
        top_x2 = (r2 * np.cos(theta2))+0.5
        top_y2 = (r2 * np.sin(theta2))+0.5

        #spinach
        r3 = 0.4 * np.sqrt(np.random.rand(12, 1))
        theta3 = 2 * np.pi * np.random.rand(12, 1)
        top_x3 = (r3 * np.cos(theta3))+0.5
        top_y3 = (r3 * np.sin(theta3))+0.5

        #pineapple
        r4 = 0.4 * np.sqrt(np.random.rand(12, 1))
        theta4 = 2 * np.pi * np.random.rand(12, 1)
        top_x4 = (r4 * np.cos(theta4))+0.5
        top_y4 = (r4 * np.sin(theta4))+0.5



        if 'tomato' in params.toppings:
            plt.plot(top_x2,top_y2,'.', color='r', markersize = 45)
    
        if 'spinach' in params.toppings:
            plt.plot(top_x3,top_y3,'.', color='g', markersize = 40)

        if 'tuna' in params.toppings:
            plt.plot(top_x1,top_y1,'.', color='darksalmon', markersize = 30)

        if 'pineapple' in params.toppings:
            plt.plot(top_x4,top_y4,'<', color='yellow', markersize = 15)           

        # slice the pizza
        x1,y1 = [-0.05, 1.05], [0.5,0.5]
        x2,y2 = [0.5, 0.5], [-0.05, 1.05]
        x3,y3 = [0.11,0.89],[0.11,0.89]
        x4,y4 = [0.11,0.89],[0.89,0.11]

        if params.slices > 1:
            plt.plot(x1,y1, color='w')
            plt.plot(x2,y2, color='w')  
        
        if params.slices > 4:
            plt.plot(x3,y3, color='w')
            plt.plot(x4,y4, color='w')  

        
        #set plot and remove axes
        plt.axis("off")
        plt.axis("equal")

        fig.tight_layout()

        # save figure
        svg_data = StringIO()
        fig.savefig(svg_data, format = 'svg')
        plt.close()

        return SVGResult(svg_data)
