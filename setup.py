from distutils.core import setup

with open('dependencies.txt') as file:
    dependencies = file.read().strip().split('\n')

setup(name='investment-visualizer',
      version='1.0',
      author='Lukas Herman',
      author_email='lukashh6@gmail.com',
      install_requires=dependencies,
      packages=['investment_visualizer'],
      )
