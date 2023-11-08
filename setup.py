from setuptools import find_packages, setup

if __name__ == '__main__':
    setup(
        name='forcedimension',
        packages=find_packages(),
        version='0.2.0b2',
        python_requires=">=3.6, <3.7",
        install_requires=[
            "setuptools>=42",
            "wheel",
            "typing_extensions >= 4.1.1, <5",
            "pydantic>=1.9.2, <2",
            "numpy>=1.16.4, <2",
            "PyYAML>=6.0.1, <7"
        ]
    )
