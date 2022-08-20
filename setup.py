
from setuptools import setup, find_packages

setup(
  name="tertran",
  version="0.1",
  packages=find_packages(),
  include_package_data=True,
  pt_modules=["tertran.py"],
  install_requires=[
    "Click"
  ],
  entry_points="""
  [console_scripts]
  tertran=src.scripts.translate:translate
  tertran-langs=src.scripts.get_langs:get_langs
  """,
)