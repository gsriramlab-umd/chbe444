import chbe444umd as des
import IPython.display as ipd

# This script displays the feasible space of a distillery allocation problem:
# max z = 5 x1 + 10 x2
# s.t.    0.05 x1 + 0.10 x2 <= 150
#         0.10 x1 + 0.05 x2 <= 150
#         0.05 x1 + 0.15 x2 <= 150
#                   0.20 x2 <= 150
#         x1, x2 >= 0

s = 0.1  # shading opacity

expressions = [{'latex': 'x_1 = x', 'hidden': 'true'},
               {'latex': 'x_2 = y', 'hidden': 'true'},
               {'latex': '0.05 x_1 + 0.10 x_2 <= 150', 'id': 'f1',
                'fillOpacity': s, 'color': '#ffbe98'},
               {'latex': '0.10 x_1 + 0.05 x_2 <= 150', 'id': 'f2',
                'fillOpacity': s, 'color': '#ffbe98'},
               {'latex': '0.05 x_1 + 0.15 x_2 <= 150', 'id': 'f3',
                'fillOpacity': s, 'color': '#ffbe98'},
               {'latex': '0.20 x_2 <= 150', 'id': 's4',
                'fillOpacity': s, 'color': '#ffbe98'},
               {'latex': 'x_1 >= 0', 'id': 'x1',
                'fillOpacity': s, 'color': '#ffbe98'},
               {'latex': 'x_2 >= 0', 'id': 'x2',
                'fillOpacity': s, 'color': '#ffbe98'},
               {'latex': '5 x_1 + 10 x_2 = z', 'id': 'obj',
                'fillOpacity': s, 'color': '#000000'}]

# A slightly better way to type the <= and >= constraints is \\\\le and \\\\ge
# This formats them more aesthetically on Desmos

# Polygon constructed from feasible space vertices
polygon = ((0, 0), (1500, 0), (1200, 600), (750, 750), (0, 750))
feasible = [{'latex': '\\\\operatorname{polygon}' + str(polygon),
             'id': 'feasible', 'fillOpacity': 0, 'color': '#006167'}]
expressions.extend(feasible)

sliders = [{'variable': 'z',
            'min': '0',
            'max': '15000',
            'step': '1000'}]

points = [{'latex': '(1200,600)',
           'color': '#000000',
           'label': 'optimum',
           'showLabel': True}]

graph_html = des.desmos_graph(expressions=expressions,
                              sliders=sliders,
                              points=points,
                              axlim=[-100, 2000, -100, 2000],
                              size=[1000, 600])

# This Python file does not display the Desmos graph directly; however,
# the following lines will save the graph to your folder in html format
# Make sure to give an appropriate name to the html file
with open('distillery_graph.html', 'w', encoding='utf-8') as f:
    f.write(graph_html.get_value())
ipd.IFrame('distillery_graph.html', width='100%', height=400)
