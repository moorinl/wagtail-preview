from setuptools import find_packages, setup


install_requires = [
    'wagtail>=2'
]

setup(
    name='wagtail-preview',
    version='0.1.0',
    description='Wagtail preview feature for StreamFields.',
    author='Rob Moorman',
    author_email='rob@moori.nl',
    url='https://github.com/moorinteractive/wagtail-preview',
    license='MIT',
    install_requires=install_requires,
    package_dir={'': 'src'},
    packages=find_packages('src'),
    include_package_data=True,
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Operating System :: Unix',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7'
    ]
)
