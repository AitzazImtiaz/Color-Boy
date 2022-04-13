from setuptools import setup

setup(
    name = "colorboy",
    version = "0.1.0",
    description = "A beautiful color printer",
    author = "AitzazImtiaz",
    url = "https://github.com/AitzazImtiaz/Color-Boy",
    packages = ["colorboy"],
    entry_points = {
        'console_scripts': [
            'colorboy = colorboy.__main__:main'
        ]
    },
)
