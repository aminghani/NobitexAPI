from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()

setup_args = dict(
    name='Nobitex',
    version='1.0.0',
    description='python nobitex api',
    long_description_content_type="text/markdown",
    long_description=README,
    license='MIT',
    packages=find_packages(),
    author='amin ghanizadeh',
    author_email='aminkhosroshahi80328@gmail.com',
    keywords=['Nobitex', 'NobitexAPI', 'pythonNobitex'],
    url='https://github.com/aminghani/NobitexAPI',
    download_url='https://pypi.org/project/elastictools/'
)

install_requires = [
    'requests'
]

if __name__ == '__main__':
    setup(**setup_args, install_requires=install_requires)