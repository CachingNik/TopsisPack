import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="topsispack-NG",
    version="0.1.1",
    author="Nikhil Gupta",
    author_email="ngupta_be17@thapar.edu",
    description="Multiple Criteria Decision Making(MCDM) using TOPSIS",
	url='https://github.com/CachingNik/TopsisPack',
	long_description=long_description,
	long_description_content_type="text/markdown",
	packages=setuptools.find_packages(),
	entry_points = {
        'console_scripts': ['Topcli=toplib.topcli:main'],
    },
	keywords = ['CLI', 'TOPSIS', 'Data'], 
	python_requires='>=2.7', 
)
