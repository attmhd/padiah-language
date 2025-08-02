from setuptools import setup, find_packages

setup(
    name='padiah-language',
    version='0.1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'padang = padiah.executor:main',
        ],
    },
    author='Muhammad Attan',
    author_email='attan@natta.stuio',
    description='Bahasa pemrograman parodi dengan sintaks Minang.',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/attmhd/padiah-language',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Interpreters',
        'Natural Language :: Indonesian',
    ],
    python_requires='>=3.10',
)
