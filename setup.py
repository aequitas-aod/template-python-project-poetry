from setuptools import setup, find_packages
import pathlib
import subprocess
import distutils.cmd

# current directory
here = pathlib.Path(__file__).parent.resolve()

version_file = here / 'VERSION'

# Get the long description from the README file
long_description = (here / 'README.md').read_text(encoding='utf-8')

# Get dependencies from the requirements.txt file
dependencies = (here / 'requirements.txt').read_text(encoding='utf-8').replace("==", ">=").splitlines()

# Get Python version from .python-version file
python_version = ">=" + (here / '.python-version').read_text(encoding='utf-8').strip()


def format_git_describe_version(version):
    if '-' in version:
        splitted = version.split('-')
        tag = splitted[0]
        index = f"dev{splitted[1]}"
        return f"{tag}.{index}"
    else:
        return version


def get_version_from_git():
    try:
        process = subprocess.run(["git", "describe", "--tags"], cwd=str(here), check=True, capture_output=True)
        version = process.stdout.decode('utf-8').strip()
        version = format_git_describe_version(version)
        with version_file.open('w') as f:
            f.write(version)
        return version
    except subprocess.CalledProcessError:
        if version_file.exists():
            return version_file.read_text().strip()
        else:
            return '0.1.0'


version = get_version_from_git()

print(f"Detected version {version} from git describe")


class GetVersionCommand(distutils.cmd.Command):
    """A custom command to get the current project version inferred from git describe."""

    description = 'gets the project version from git describe'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        print(version)


class GetMinimumPythonVersion(distutils.cmd.Command):
    """A custom command to get the current project commands inferred from `requirements.txt`."""

    description = 'gets the project\'s minimum Python version from `.python-version`'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        print(".".join(python_version[2:].split(".")[:2]))


url = 'https://github.com/aequitas-aod/my_project'


setup(
    name='my_project',  # Required
    version=version,
    description='Description of the project here',
    license='Apache 2.0 License',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url=url,
    author='Name Surname',
    author_email='name.surname@organization.domain',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only'
    ],
    keywords='aeuitas, horizon2020, xai, bias',  # Optional
    # package_dir={'': 'src'},  # Optional
    packages=find_packages(),  # Required
    include_package_data=True,
    python_requires=python_version,
    install_requires=dependencies,
    zip_safe=False,
    platforms="Independant",
    project_urls={  # Optional
        'Bug Reports': f'{url}/issues',
        # 'Funding': 'https://donate.pypi.org',
        # 'Say Thanks!': 'http://saythanks.io/to/example',
        'Source': url,
    },
    cmdclass={
        'get_project_version': GetVersionCommand,
        'get_minimum_python_version': GetMinimumPythonVersion,
    },
)
