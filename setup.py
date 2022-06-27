from pathlib import PosixPath

from setuptools import setup, find_packages

SELF_PATH = PosixPath(__file__).parent.absolute()
VERSION = '1.0.0'


if __name__ == '__main__':
    with open(SELF_PATH / 'README.md', encoding='utf8') as fd:
        long_description = fd.read()

    with open(SELF_PATH / 'requirements.txt', encoding='utf8') as fd:
        install_requires = [li for li in fd.readlines() if li and not li.startswith('#')]

    with open(SELF_PATH / 'requirements-test.txt', encoding='utf8') as fd:
        test_requires = [li for li in fd.readlines() if li and not (li.startswith('#') or li.startswith('-r'))]

    setup(
        name='osb',
        version=VERSION,
        description='otus space battle',
        long_description=long_description,
        python_requires='>=3.7.9',
        author='test',
        author_email='test@test.ru',
        url='',
        packages=find_packages(where="src"),
        package_dir={"": "src"},
        install_requires=install_requires,
        extras_require={
            'test': test_requires,
        },
    )
