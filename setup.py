from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in zineify/__init__.py
from zineify import __version__ as version

setup(
	name="zineify",
	version=version,
	description="Everydauy zines",
	author="Kamal Johnson",
	author_email="kamal@frappe.io",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires,
)
