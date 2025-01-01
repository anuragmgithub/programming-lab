from setuptools import setup, find_packages

setup(
    name='package_build',  # Name of your package
    version='0.1',  # Initial version
    packages=find_packages(),  # This automatically finds and includes your package
    install_requires=[],  # Any dependencies can be listed here (empty in this case)
    author='Anurag Mishra',
    author_email='your.email@example.com',
    description='A simple greeting and farewell package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/my_package',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
)
