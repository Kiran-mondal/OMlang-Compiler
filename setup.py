from setuptools import setup

setup(
    name="omlang",
    version="3.6.1",
    description="OMlang: A strictly English data science and visualization programming language.",
    author="Kiran Mondal",
    py_modules=["om"],
    install_requires=[
        # Core Runtime Ecosystem Dependencies
        "numpy>=1.20.0",
        "pandas>=1.3.0",
        "polars>=0.19.0",
        "torch>=2.0.0",
        "seaborn>=0.12.0",
        "matplotlib>=3.5.0",
        "plotly>=5.10.0",
    ],
    entry_points={
        "console_scripts": [
            "om=om:cli",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
