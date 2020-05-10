from setuptools import setup

with open("README.md", 'r') as f:
	long_description = f.read()

setup(
	name='Quagga',
	version='1.0',
	description='An email segmentation system',
	license="GPL",
	long_description=long_description,
	author='Tim Repke, Ben Hurdelhey',
	author_email='tim.repke@hpi.de',
	url="",
	packages=['Quagga', 'Quagga.Utils', 'Quagga.Utils.BlockParser', 'Quagga.Utils.Annotation', 'Quagga.Utils.Reader'],
	package_data={'': ['models/*/*.json', 'models/*/*.hdf5', 'static/index.html']},
	install_requires=['absl-py==0.7.0', 'astor==0.7.1', 'bleach==1.5.0', 'click==6.7',
	                  'cycler==0.10.0', 'dateparser@git+https://github.com/scrapinghub/dateparser.git@a01a4d2071a8f1d4b368543e5e09cde5eb880799', 'Flask==1.0.2', 'gast==0.2.2', 'grpcio==1.14.0', 'h5py==2.8.0',
	                  'html5lib==0.9999999', 'itsdangerous==0.24', 'Jinja2==2.10',
	                  'kiwisolver==1.0.1', 'Markdown==2.6.11', 'MarkupSafe==1.1', 'matplotlib==3.0.0', 'nose==1.3.7', 'numpy==1.17.0',
	                  'pandas==0.24.2', 'protobuf==3.6.1', 'pyparsing==2.2.0', 'python-dateutil==2.7.3', 'pytz==2018.5', 'python-Levenshtein',
	                  'PyYAML==5.3', 'scikit-learn==0.22.0', 'scipy==1.3.1', 'six==1.11.0',
	                  'sklearn', 'tensorflow==1.15', 'termcolor==1.1.0',
	                  'Werkzeug==0.14.1'],
)
