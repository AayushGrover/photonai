from distutils.core import setup
from setuptools import find_packages
import photonai

setup(
  name='photonai',
  packages=find_packages(),
  include_package_data=True,
  version="0.1.8",
  description='A Python-Based Hyperparameter optimization Toolbox for Neural Networks',
  author='PHOTON Team',
  author_email='hahnt@wwu.de',
  url='https://github.com/photonai-team/photonai.git',
  download_url='https://github.com/photonai-team/photonai/archive/0.1.8.tar.gz',
  keywords=['machine learning', 'deep learning', 'neural networks', 'hyperparameter'],
  classifiers=[],
  install_requires=[
        'numpy',
        'matplotlib',
        'tensorflow',
        'slackclient',
        'progressbar2',
        'Pillow',
        'scikit-learn',
        'keras',
        'nilearn',
        'pandas',
        'nibabel',
        'pandas',
        'six',
        'h5py',
        'xlrd',
        'plotly',
        'imblearn',
        'pymodm',
        'scipy',
        'statsmodels',
        'flask'
  ]
)
