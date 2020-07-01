from setuptools import setup

if __name__ == "__main__":
    setup(
        install_requires=["numpy", "matplotlib", "dataclasses"],
        extras_require={"tests": ["pytest"],},
    )
