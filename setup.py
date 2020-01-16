from setuptools import setup, find_packages

with open('README.md', encoding='UTF-8') as f:
    readme = f.read()

setup(
        name='userinfotool',
        version='1.0.0',
        description='Command line tool to export user info in either JSON format or CSV format',
        long_description=readme,
        author='Karanveer Singh Jhala',
        author_email='karanjhala@gmail.com',
        packages=find_packages('src'),
        package_dir={'':'src'},
        install_requires=[]
)

