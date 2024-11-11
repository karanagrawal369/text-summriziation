import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "Text-Summarizer-Project"
AUTHOR_USER_NAME = "karanagrawal369"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "karanagrawal027@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for NLP app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    install_requires=[
        "transformers",
        "datasets",
        "sacrebleu",
        "rouge_score",
        "py7zr",
        "pandas",
        "nltk",
        "tqdm",
        "PyYAML",
        "matplotlib",
        "torch",
        "notebook",
        "boto3",
        "mypy-boto3-s3",
        "python-box==6.0.2",
        "ensure==1.0.2",
        "fastapi==0.78.0",
        "uvicorn==0.18.3",
        "Jinja2==3.1.2",
    ]
)
