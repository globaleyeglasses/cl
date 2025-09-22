from setuptools import setup, find_packages

setup(
    name="cocoleni_optics",
    version="0.1.0",
    description="COCO LENI Optics App with Prescription, Lens Order, and Face Scan 3D",
    author="COCO LENI",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["frappe>=15.0.0"],
    zip_safe=False,
)
