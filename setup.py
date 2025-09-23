from setuptools import setup, find_packages

setup(
    name="cocoleni_optics",
    version="0.3.2",
    description="COCO LENI Optics: DocTypes, Workspace (title fix), Sales Order header & item links",
    author="COCO LENI",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["frappe>=15.0.0"],
    zip_safe=False,
)
