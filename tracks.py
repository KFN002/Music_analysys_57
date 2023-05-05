import numpy as np
import pandas as pd
import ast
from matplotlib import pyplot as plt

df = pd.read_csv('tracks.csv')


'''
1. Составить (и вывести) таблицу следующего состава:
<Номер строки> <Трек> <Исполнитель>
2. Построить зависимости energy(loudness), energy(tempo) energy(time_signature) графиком scatter
'''


class TrackTable:
    def __init__(self, table='tracks.csv'):
        self.df = pd.read_csv(table)

    def show_tracks(self):
        tracks = []
        for num, row in enumerate(self.df.values):
            if num > 10:
                break
            line = f'{num}-{row[1].strip()}-{"".join(ast.literal_eval(row[5])).strip()}'
            print(line)
            tracks.append(line)
        return tracks

    def make_scatter_graph(self, graph_type=1):
        colors = np.random.rand(len(self.df))
        if graph_type == 1:
            x = self.df['energy']
            y = self.df['loudness']
        elif graph_type == 2:
            x = self.df['energy']
            y = self.df['tempo']
        else:
            x = self.df['energy']
            y = self.df['time_signature']
        plt.scatter(x, y, c=colors, alpha=0.5)
        plt.show()


obj = TrackTable('tracks.csv')
obj.show_tracks()
obj.make_scatter_graph()
