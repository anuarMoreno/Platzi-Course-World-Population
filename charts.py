#Modulo para graficar los datos.

import matplotlib.pyplot as plt

def generate_bar_chart(labels,values,country):
  fig, ax = plt.subplots()
  ax.bar(labels,values)
  ax.set(xlabel='Years', ylabel='Population', title=country)
  plt.show()

def generate_pie_chart(labels,values):
  fig, ax = plt.subplots()
  ax.pie(values, labels=labels)
  ax.axis('equal')
  plt.show()


if __name__ == '__main__':
 print('EJECUTANDO EL SCRIPT DIRECTAMENTE')
