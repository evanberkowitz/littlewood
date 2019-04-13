import setuptools

with open("README.md", 'r') as readme:
    long_description = readme.read()

setuptools.setup(
    name="littlewood",
    version="0.0.1",
    author="Evan Berkowitz",
    author_email="littlewood@evanberkowitz.com",
    description="Visualize roots of classes of polynomials",
    long_description="text/markdown",
    url="https://github.com/evanberkowitz/littlewood",
    scripts=['scripts/littlewood'],
    packages=setuptools.find_packages(),
)
