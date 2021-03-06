import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="drlgeb",
    version="0.0.1",
    author="geb",
    author_email="853934146@qq.com",
    description="A sample but effective drl lib.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mikuh/drlgeb",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['numpy', 'tensorflow', 'gym', 'gym[atari]'],
    python_requires='>=3.7',
)
