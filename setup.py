"""Setup.py for the Astronomer sample Airflow provider package. Built from datadog provider package for now."""

from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

"""Perform the package airflow-provider-voltdb setup."""
setup(
    name='airflow-provider-voltdb',
    version="0.0.1",
    description='A VoltDB provider package built by Data platform.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    entry_points={
        "apache_airflow_provider": [
            "provider_info=voltdb_provider.__init__:get_provider_info"
        ]
    },
    license='Apache License 2.0',
    packages=['voltdb', 'voltdb.hooks',
              'voltdb.sensors', 'voltdb.operators'],
    install_requires=['apache-airflow>=2.0'],
    setup_requires=['setuptools', 'wheel'],
    author='Data platform',
    author_email='sample@sample.com',
    python_requires='~=3.7',
)
