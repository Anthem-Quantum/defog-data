from setuptools import setup

setup(
    name="defog-data",
    version="0.1.1",
    description="Static SQL and JSON files containing the data we use for evaluations",
    author="Defog",
    author_email="support@defog.ai",
    py_modules=["defog_data", "gen_embeddings"],
    install_requires=[],
)
