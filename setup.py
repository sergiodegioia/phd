from setuptools import setup
import versioneer

requirements = [
    # package requirements go here
]

setup(
    name='phd',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description="trial",
    license="GNUv3",
    author="Sergio de Gioia",
    author_email='sergiodegioia@gmail.com',
    url='https://github.com/sergiodegioia/phd',
    packages=['thepackage'],
    entry_points={
        'console_scripts': [
            'thepackage=thepackage.cli:cli'
        ]
    },
    install_requires=requirements,
    keywords='phd',
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ]
)
