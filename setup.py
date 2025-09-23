from setuptools import setup, find_packages

setup(
    name="cocoleni_optics",
    version="0.3.1",
    description="COCO LENI Optics: DocTypes + Workspace + Sales Order links (header & item)",
    author="COCO LENI",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["frappe>=15.0.0"],
    zip_safe=False,
)
