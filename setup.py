import sys
from setuptools import setup

tests_require = ["nose>=1.0"]
if sys.version_info < (3,0):
    tests_require = ["nose>=1.0", "mock"]

setup(
    name="helm",
    version="0.1.0",
    author="iovetux",
    author_email="me@ilovetux.com",
    description="A template as a service utility...you know, for DevOps",
    license="GPLv3",
    keywords="template reports",
    url="http://github.com/ilovetux/helm",
    packages=['helm'],
    install_requires=["colorama", "jinja2"],
    entry_points={
        "console_scripts": [
            "helm=helm.cli:main",
        ],
        "helm.InputPlugin": [
            "CsvInput=helm:CsvInput",
            "JsonInput=helm:JsonInput",
        ]
    },
    test_suite="nose.collector",
    tests_require=tests_require,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Utilities",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
