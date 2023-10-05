from setuptools import setup

if __name__ == '__main__':
    setup(
        name='forcedimension',
        version='0.1.0',
        python_requires=">=3.6, <3.7",
        install_requires=[
            "setuptools>=42",
            "wheel",
            "typing_extensions >= 4.1.1, <5",
            "pydantic>=1.9.2, <2",
            "numpy>=1.16.4, <2"
        ]
    )
