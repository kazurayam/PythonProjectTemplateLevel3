from setuptools import setup, find_packages

setup(
    name="flaskr-kazurayam",
    version="1.0",
    description="Flask Tutorial",
    author="kazurayam",
    author_email="kazu@gmail.com",
    url="https://github.com/kazurayam/PythonProjectTemplateLevel3",
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    entry_points="""
      [console_scripts]
      hello = hello:hello 
    """,
    install_requires=open('requirements.txt').read().splitlines(),
)