#!/usr/bin/python3

import matplotlib.pyplot as plt
from argparse import ArgumentParser

class Visualizer():
    def __init__(self, starting_money=0, projected_years=10, return_rate=0.08, monthly=120):
        plt.style.use('seaborn-darkgrid')

        self.starting_money = starting_money
        self.projected_years = projected_years
        self.return_rate = return_rate
        self.monthly = monthly

    def yrange(self, start=0, stop=12, step=1/12):
        while start <= stop:
            yield start
            start += step

    def get_projected_values(self):
        projected_values = []
        return_func = lambda x: x + self.monthly + self.return_rate * (x + self.monthly) / 12

        projected_values.append(self.starting_money)
        for _ in self.yrange(start=1/12, stop=self.projected_years):
            projected_values.append(return_func(projected_values[-1]))

        return projected_values

    def visualize(self):
        x = list(self.yrange(stop=self.projected_years))
        y = self.get_projected_values()
        title = 'Projected Investment Values in ' + str(self.projected_years) + ' Years'
        xlabel = 'Year'
        ylabel = 'Projected Value in $'

        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.plot(x, y)

        plt.show()
        print('Final projected value is ${:,.2f}'.format(y[-1]))

def main():
    parser = ArgumentParser()
    parser.add_argument('-s', '--starting_money', help='default is 0', type=float, default=0)
    parser.add_argument('-p', '--projected_years', help='default is 10', type=int, default=10)
    parser.add_argument('-r', '--return_rate', help='default is 0.08', type=float, default=0.08)
    parser.add_argument('-m', '--monthly', help='default is 120', type=float, default=120)
    args = parser.parse_args()

    visualizer = Visualizer(args.starting_money, args.projected_years, args.return_rate,
                            args.monthly)
    visualizer.visualize()

if __name__ == '__main__':
    main()
