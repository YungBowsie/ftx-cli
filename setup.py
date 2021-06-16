from setuptools import setup, find_packages

setup(
    name="ftx_cli",
    license="MIT",
    packages=find_packages(),
    include_package_data=True,
    # Add command line: ftx
    entry_points={
        "console_scripts": ["ftx=ftx_cli.cli:main",
        "ftx-cli=ftx_cli.cli:main"]
    },

    # PyPI metadata
    author="YungBowsie",
    author_email="yungbowsie@protonmail.com",
    description="Python based CLI to quickly work with FTX's API plus helper classes and functions to help you do custom things faster.",
    keywords="ftx portfolio tool",
)