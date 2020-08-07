
# Use this command for deploy.
#   python3 setup.py sdist bdist_wheel && python3 -m twine upload --skip-existing dist/*

import io
from setuptools import find_packages, setup

setup(name='cloud_scheduler',
      version='0.1',
      description='This package makes it easy to manage Glue Crawler and Cloudwatch schedulers on AWS services. You can schedule lambda function execution, etc.',
      long_description="Please refer to the https://github.com/da-huin/cloud_scheduler",
      long_description_content_type="text/markdown",
      url='https://github.com/da-huin/cloud_scheduler',
      download_url= 'https://github.com/da-huin/cloud_scheduler/archive/master.zip',
      author='JunYeong Park',
      author_email='dahuin000@gmail.com',
      license='MIT',
      packages=find_packages(),
      install_requires=[],
      classifiers=[
          'Programming Language :: Python :: 3',
    ]
)

