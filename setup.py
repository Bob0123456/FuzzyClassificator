#!/usr/bin/env python
# -*- coding: utf-8 -*-


from setuptools import setup
import os

__version__ = '1.3'  # identify main version of FuzzyClassificator
devStatus = '4 - Beta'  # default build status, see: https://pypi.python.org/pypi?%3Aaction=list_classifiers

if 'TRAVIS_BUILD_NUMBER' in os.environ and 'TRAVIS_BRANCH' in os.environ:
    print("This is TRAVIS-CI build")
    print("TRAVIS_BUILD_NUMBER = {}".format(os.environ['TRAVIS_BUILD_NUMBER']))
    print("TRAVIS_BRANCH = {}".format(os.environ['TRAVIS_BRANCH']))

    __version__ += '.{}{}'.format(
        '' if 'release' in os.environ['TRAVIS_BRANCH'] or os.environ['TRAVIS_BRANCH'] == 'master' else 'dev',
        os.environ['TRAVIS_BUILD_NUMBER'],
    )

    devStatus = '5 - Production/Stable' if 'release' in os.environ['TRAVIS_BRANCH'] or os.environ['TRAVIS_BRANCH'] == 'master' else devStatus

else:
    print("This is local build")
    __version__ += '.dev0'  # set version as major.minor.localbuild if local build: python setup.py install

print("FuzzyClassificator build version = {}".format(__version__))


setup(
    name='FuzzyClassificator',

    version=__version__,

    description='This program uses neural networks to solve classification problems, and uses fuzzy sets and fuzzy logic to interpreting results.',

    long_description='You can see detailed user manual here: https://devopshq.github.io/FuzzyClassificator/',

    license='MIT',

    author='Timur Gilmullin',

    author_email='tim55667757@gmail.com',

    url='https://devopshq.github.io/FuzzyClassificator/',

    download_url='https://github.com/devopshq/FuzzyClassificator.git',

    entry_points={'console_scripts': ['FuzzyClassificator = fuzzyclassificator.FuzzyClassificator:Main']},

    classifiers=[
        'Development Status :: {}'.format(devStatus),
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
    ],

    keywords=[
        'classificating',
        'clustering',
        'classificator',
        'fuzzy',
        'logic',
        'math',
        'science',
        'research',
    ],

    packages=[
        'fuzzyclassificator',

        'pybrain',
        'pybrain.auxiliary',
        'pybrain.datasets',
        'pybrain.optimization',
        'pybrain.optimization.distributionbased',
        'pybrain.optimization.finitedifference',
        'pybrain.optimization.memetic',
        'pybrain.optimization.populationbased',
        'pybrain.optimization.populationbased.coevolution',
        'pybrain.optimization.populationbased.multiobjective',
        'pybrain.rl.agents',
        'pybrain.rl.environments',
        'pybrain.rl.environments.cartpole',
        'pybrain.rl.environments.cartpole.fast_version',
        'pybrain.rl.environments.classic',
        'pybrain.rl.environments.flexcube',
        'pybrain.rl.environments.functions',
        'pybrain.rl.environments.mazes',
        'pybrain.rl.environments.mazes.tasks',
        'pybrain.rl.environments.ode',
        'pybrain.rl.environments.ode.instances',
        'pybrain.rl.environments.ode.models',
        'pybrain.rl.environments.ode.tasks',
        'pybrain.rl.environments.ode.tools',
        'pybrain.rl.environments.shipsteer',
        'pybrain.rl.environments.simple',
        'pybrain.rl.environments.simplerace',
        'pybrain.rl.environments.twoplayergames',
        'pybrain.rl.environments.twoplayergames.capturegameplayers',
        'pybrain.rl.environments.twoplayergames.gomokuplayers',
        'pybrain.rl.environments.twoplayergames.tasks',
        'pybrain.rl.experiments',
        'pybrain.rl.explorers',
        'pybrain.rl.explorers.continuous',
        'pybrain.rl.explorers.discrete',
        'pybrain.rl.learners',
        'pybrain.rl.learners.directsearch',
        'pybrain.rl.learners.meta',
        'pybrain.rl.learners.modelbased',
        'pybrain.rl.learners.valuebased',
        'pybrain.structure',
        'pybrain.structure.connections',
        'pybrain.structure.evolvables',
        'pybrain.structure.modules',
        'pybrain.structure.networks',
        'pybrain.structure.networks.custom',
        'pybrain.supervised',
        'pybrain.supervised.evolino',
        'pybrain.supervised.knn',
        'pybrain.supervised.knn.lsh',
        'pybrain.supervised.trainers',
        'pybrain.tools',
        'pybrain.tools.customxml',
        'pybrain.tools.datasets',
        'pybrain.tools.mixtures',
        'pybrain.tools.networking',
        'pybrain.tools.plotting',
        'pybrain.unsupervised',
        'pybrain.unsupervised.trainers',
    ],

    setup_requires=[
    ],

    tests_require=[
        'pytest',
    ],

    install_requires=[
    ],

    package_data={
        '': [
            './tests/*.py',
            
            'candidates.dat',
            'ethalons.dat',
            'network.xml',
            'report.txt',
            
            'LICENSE',
            'README.md',
            'classification_process.*',
        ],
    },

    zip_safe=True,
)
