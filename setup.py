import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(name='wronnay_search_lib',
      version='1.0.1',
      description='A library of classes which can be used to build a search engine.',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='https://github.com/Wronnay/search-lib',
      author='Christoph Miksche',
      license='GPLv3',
      classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
            "Operating System :: Unix",
      ],
      keywords=['wronnay', 'search', 'lib', 'crawler'],
      install_requires=[
            'beautifulsoup4',
            'lxml',
            'mongoengine'
      ],
      packages=setuptools.find_packages()
      )
