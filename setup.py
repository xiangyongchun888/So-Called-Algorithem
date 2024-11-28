from setuptools import setup, find_packages

setup(
    name="ycalg",
    version="0.1.0",
    description="A funny algorithm package",
    author="Yongchun",
    author_email="xiangyongchun888@gmail.com",
    packages=find_packages(),
    install_requires=[
        "numpy>=1.21",
        "requests>=2.25",
    ],
    python_requires=">=3.6",
)
