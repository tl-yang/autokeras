from distutils.core import setup
from setuptools import find_packages

setup(
    name='autokeras',
    packages=find_packages(exclude=('tests',)),
    install_requires=['torch==0.4.1', 'torchvision==0.2.1', 'numpy>=1.14.5', 'keras==2.2.2', 'scikit-learn==0.19.1',
                      'tensorflow==1.10.0', 'tqdm==4.25.0', 'imageio', 'GPUtil'],
    version='0.2.19',
    description='AutoML for deep learning',
    author='Haifeng Jin',
    author_email='jhfjhfj1@gmail.com',
    url='http://autokeras.com',
    download_url='https://github.com/jhfjhfj1/autokeras/archive/0.2.19.tar.gz',
    keywords=['automl'],  # arbitrary keywords
    classifiers=[]
)
