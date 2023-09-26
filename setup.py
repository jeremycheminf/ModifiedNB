from setuptools import setup

setup(
    name='ModifiedNB',
    version='0.3',
    author='Eloy Félix- update Jérémy Besnard',
    author_email='eloyfelix@gmail.com',
    description='Laplace corrected modified naïve bayes model',
    url='https://github.com/chembl/ModifiedNB/',
    license='MIT',
    packages=[
        'ModifiedNB',
        ],
    long_description=open('README.md', encoding='utf-8').read(),
    install_requires=[
        'scikit-learn>=1.3.0',
    ],
    include_package_data=True,
    classifiers=['License :: OSI Approved :: MIT License',
                 'Programming Language :: Python :: 3.10',
                 'Topic :: Scientific/Engineering :: Chemistry'],
    zip_safe=False,
)
