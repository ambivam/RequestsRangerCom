from setuptools import setup

setup(name='Distutils',
      version='1.0',
      description='Python Distribution Utilities',
      author='Rajani Kanth',
      url='https://gitlab.com/XP2-CognitiveIntake/cogx-test-framework.git',
      packages=['xpmsrequests','xpmsrequests.data','xpmsrequests.data.images','xpmsrequests.data.jsonfiles','xpmsrequests.reqscripts','xpmsrequests.testscriptscogx'],
      install_requires=['requests','allure-pytest','allure-python-commons','pytest'],
      )