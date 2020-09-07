from setuptools import setup
install_requires = [
    "pyyaml",
    "inquirer",
]


setup(
    name='boip',
    version='0.1',
    install_requires=install_requires,
    tests_require="pytest",
)
