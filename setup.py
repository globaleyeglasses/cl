from setuptools import setup, find_packages

setup(
    name="cocoleni_optics",
    version="0.1.0",
    description="COCO LENI Optics Frappe app (Optics Retail: Prescription, Lens Order, 3D Face Scan)",
    author="COCO LENI",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["frappe>=15.0.0"],
    zip_safe=False,
)
