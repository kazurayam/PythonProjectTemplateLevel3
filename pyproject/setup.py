from setuptools import setup, find_packages

setup(
    name="mypkg-kazurayam",
    version="1.0",
    description="simplest python package that greets you",
    author="kazurayam",
    author_email="kazu@gmail.com",
    url="https://github.com/kazurayam/PythonProjectTemplateLevel2",
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    entry_points="""
      [console_scripts]
      greeting = mypkg.cli:main 
    """,
    install_requires=open('requirements.txt').read().splitlines(),
)