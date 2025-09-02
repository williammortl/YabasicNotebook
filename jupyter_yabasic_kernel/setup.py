from setuptools import setup

setup(
    name='jupyter_yabasic_kernel',
    version='0.1',
    description='A Jupyter kernel for BASIC using yabasic',
    author='William M Mortl',
    packages=['jupyter_yabasic_kernel'],
    install_requires=['ipykernel'],
    include_package_data=True,
    entry_points={
        'console_scripts': [
        ],
    },
)
