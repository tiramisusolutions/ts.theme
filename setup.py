from setuptools import setup, find_packages
import os

version = open(os.path.join("ts", "theme", "version.txt")).read().strip()

setup(name='ts.theme',
      version=version,
      description="Diazo theme for Tiramisu Solutions",
      long_description=open(os.path.join("docs", "README.txt")).read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Plone",
        "Framework :: Plone :: 4.3",
        ],
      keywords='',
      author='Sven Strack',
      author_email='sven@tiramisu.solutions',
      url='http://tiramisu.solutions',
      license='gpl',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['ts'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'plone.app.theming',
          # -*- Extra requirements: -*-
      ],
      extras_require = {
            'test': [
                    'plone.app.testing',
                ]
      },
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
)
