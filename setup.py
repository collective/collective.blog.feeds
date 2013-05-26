from setuptools import setup, find_packages
import os

version = open(os.path.join("collective", "blog", "feeds", "version.txt")).read().strip()

setup(name='collective.blog.feeds',
      version=version,
      description="Provides several syndication feed types for standard folders.",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Framework :: Plone :: 4.0",
        "Framework :: Plone :: 4.1",
        "Framework :: Plone :: 4.2",
        "Framework :: Plone :: 4.3",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        ],
      keywords='plone blog rss podcast feeds',
      author='Jarn AS',
      author_email='info@jarn.com',
      url='http://svn.plone.org/svn/collective/collective.blog.feeds',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective', 'collective.blog'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'Products.fatsyndication',
          'Plone',
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
