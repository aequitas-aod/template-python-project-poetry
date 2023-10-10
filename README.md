# Python project template

A simple template of a Python project, with a rigid file structure, and predisposition for unit testing and release on PyPi.

## Relevant features

- All your project code into a single main package (`my_project/`)
- All your project tests into a single test package (`test/`)
- Unit testing support via [`unittest`](https://docs.python.org/3/library/unittest.html)
- Automatic testing on all branches via GitHub Actions
- Semi-automatic versioning via Git
- Packaging support via [`setuptools`](https://setuptools.pypa.io/en/latest/setuptools.html)
- Automatic release on [PyPi](https://pypi.org/) via GitHub Actions
- Docker image support via `Dockerfile`
- Automatic release on [DockerHub](https://hub.docker.com/) via GitHub Actions
- Support for semi-automatic development environment management via [Pyenv](https://github.com/pyenv/pyenv)
- Automatic dependencies updates via [Renovate](https://docs.renovatebot.com/)
- Automatic conversion of `TODO` comments into GitHub issues via the `alstr/todo-to-issue-action`

## Project structure 

Overview:
```bash
<root directory>
├── my_project/             # main package (should be named after your project)
│   ├── __init__.py         # python package marker
│   └── __main__.py         # application entry point
├── test/                   # test package (should contain unit tests)
├── .github/                # configuration of GitHub CI
│   └── workflows/          # configuration of GitHub Workflows
│       ├── check.yml       # runs tests on multiple OS and versions of Python
│       └── deploy.yml      # if check succeeds, and the current branch is one of {main, master}, triggers automatic releas on PyPi
├── MANIFEST.in             # file stating what to include/exclude in releases 
├── LICENSE                 # license file (Apache 2.0 by default)
├── pyproject.toml          # declares build dependencies
├── renovate.json           # configuration of Renovate bot, for automatic dependency updates
├── requirements-dev.txt    # declares development dependencies
├── requirements.txt        # declares runtime dependencies
├── setup.py                # configuration of the package to be released on Pypi
└── Dockerfile              # configuration of the Docker image to be realsed on Dockerhub
```

## TODO-list for template usage

1. Use this template to create a new GitHub repository, say `my_project`
    - this name will also be used to identify the package on PyPi
        + so, we suggest choosing a name which has not been used on PyPi, yet
        + we also suggest choosing a name which is a valid Python package name (i.e. `using_snake_case`)

2. Clone the `my_project` repository

3. Open a shell into your local `my_project` directory and run 
    ```bash
    ./rename-template.sh my_project
    ``` 
    
    This will coherently rename the template's project name with the one chosen by you (i.e. `my_project`, in this example)

4. Commit & push

5. Ensure you like the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0.html). If you don't, change the content of the `LICENSE` file

6. Ensure the version reported in `.python-version` corresponds to the actual Python version you are willing to use to develop your project

7. Check the Python version and OS tests should be run on in CI, by looking the file `.github/workflows/check.yml`

8. Add your runtime dependencies to `requirements.txt`
    + and development-only dependencies here `requirements-dev.txt`

9. Set your project's release metadata and dependencies by editing `setup.py`

10. Change the assignee for pull-requests for automatic dependency updates by editing `renovate.json`
    + currently defaults to @gciatto

11. Add your PyPi credentials as secrets of the GitHub repository 
    - `PYPI_USERNAME` (resp. `PYPI_PASSWORD`) for your username (resp. password)
    - this may require you to register on PyPi first

12. Generate a GitHub token and add it as a secret of the GitHub repository, named `RELEASE_TOKEN`
    - cf. <https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-personal-access-token-classic>
    - the token must allow pushing to the repository

13. Put your main (resp. test) code in `my_project/` (resp. `test/`)

## How to do stuff

### Run your code as an application

This will execute the file `my_project/__main__.py`:
```bash
python -m my_project 
```

### Run unit tests

```bash
python -m unittest discover -s test -t .
```

> Tests are automatically run in CI, on all pushes on all branches.
> There, tests are executed on multiple OS (Win, Mac, Ubuntu) and on multiple Python versions (from `3.8` to `3.11`).

### Restore dev dependencies

```bash
pip install -r requirements-dev.txt
```

### Release a new version on PyPi

> This paragraph is more understandable if the reader has some background about [GitFlow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow)

GitHub actions automatically release a new version of `my_project` on PyPi whenever commits are pushed on either the `main`/`master` or `develop` branches, as well as when new tags are pushed.

Tags are assumed to consist of [semantic versioning](https://semver.org/) strings of the form `Major.Minor.Patch` where `Major`, `Minor`, and `Patch` are non-negative integers.

So, to release version `X.Y.Z`, developers must:

1. tag a commit on the `master`/`main`/`develop` branch, using `X.Y.Z` as the tag label
    ```bash
    git tag -a 'X.Y.Z' -m <a message here describing the version>
    ```

2. push the tag
    ```bash
    git push --follow-tags
    ```

3. GitHub Actions will then run tests and, if all of them succeed, release the code on PyPi.
After the release, users will be able to install your code via Pip.

> Non-tagged commits pushed on the `master`/`main`/`develop` branch will trigger __dev releases__.
> Dev releases are automatically tagged as `X.Y.Y.devN`, where
> - `X.Y.Y` is the value of the __most recent__ version tag
> - `N` is the amount of commits following the most recent version tag 
