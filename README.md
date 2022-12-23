# Python project template

A simple template of a Python project, with a rigid file structure, and predisposition for unit testing and release on PyPi.

## Project structure 

Overview:
```bash
<root directory>
├── my_project/			    # main package (should be named after your project)
│   ├── __init__.py		    # python package marker
│   └── __main__.py		    # application entry point
├── test/				    # test package (should contain unit tests)
├── .github/			    # configuration of GitHub CI
│   ├── scripts/		    # contains bash script to be used in CI
│   │   └── retry.sh	    # script automating timed retry of release operations
│   └── workflows/			# configuration of GitHub Workflows
│       ├── check.yml 		# runs tests on multiple OS and versions of Python
│       ├── deploy.yml 		# if check succeeds, and the current branch is one of {main, master, develop}, triggers automatic releas on PyPi
│       └── dockerify.yml  	# if deploy succeeds, builds a Docker image and pushes it on DockerHub 
├── MANIFEST.in			    # file stating what to include/exclude in releases 
├── LICENSE				    # license file (Apache 2.0 by default)
├── pyproject.toml		    # declares build dependencies
├── renovate.json		    # configuration of Renovate bot, for automatic dependency updates
├── requirements.txt	    # declares development dependencies
├── setup.py			    # configuration of the package to be released on Pypi
└── Dockerfile			    # configuration of the Docker image to be realsed on Dockerhub
```
