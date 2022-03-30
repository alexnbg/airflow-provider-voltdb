from setuptools import setup, find_packages

with open("README.md", "r") as readme:
    long_description = readme.read()

setup(name='airflow-provider-voltdb',
      version="1.0.3",
      description='VoltDB provider package',
      long_description=long_description,
      long_description_content_type='text/markdown',
      entry_points={
          "apache_airflow_provider": [
              "provider_info=voltdb_provider.get_provider_info:get_provider_info"
          ]
      },
      packages=[
          'voltdb_provider',
          'voltdb_provider.hooks',
      ],
      install_requires=['apache-airflow>=2.0'],
      setup_requires=['setuptools', 'wheel'],
      author='Data Platform',
      author_email='data.platform@ft.com',
      url='None',
      )
