from setuptools import setup
install_requires = [
    "pyyaml",
    "inquirer",
]


setup(
    name='mayaqt-generator',
    version='0.1',
    install_requires=install_requires,
    tests_require="pytest",
)
