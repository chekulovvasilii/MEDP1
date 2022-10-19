import matplotlib.pyplot as plt
import numpy as np
import os
from lxml import etree as et

#plt.style.use('seaborn-whitegrid')

if not os.path.isdir("results"):
    os.mkdir("results")

if __name__ == '__main__':
    A = 0
    x = np.arange(-5.12, 5.12, 0.01)
    y = -(1+np.cos(12*np.sqrt(x**2+A**2)))/(0.5*(x**2+A**2)+2)

    x_str = [str(j) for j in x]
    y_str = [str(j) for j in y]

    y_graph = -(1+np.cos(12*np.sqrt(x**2+A**2)))/(0.5*(x**2+A**2)+2)
    plt.plot(x, y_graph)
    plt.show()

    if not os.path.isdir("results"):
        os.mkdir("results")

    data = et.Element('data')
    for i in range(len(x_str)):
        row = et.SubElement(data, 'row')
        x_res = et.SubElement(row, 'x').text = str(x_str[i])
        y_res = et.SubElement(row, 'y').text = str(y_str[i])

    xml_file = et.tostring(data, encoding='unicode')
    with open(r'results\results.xml', "w") as file:
        file.write(xml_file)
