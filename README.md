# whisk: The easy-bake ML project structure

[![pypi](https://img.shields.io/pypi/v/whisk.svg)](https://pypi.python.org/pypi/whisk)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/whisk)](https://pypi.python.org/pypi/whisk)
[![docs](https://readthedocs.org/projects/whisk/badge/?version=latest)](https://whisk.readthedocs.io/en/latest/?badge=latest)

__whisk is an open-source ML project framework that makes collaboration, reproducibility, and deployment "just work".__ It combines a suite of lightweight tools with a logical and flexible project structure. Release your model to the world without a software engineer.

Whisk doesn't lock you into a particular ML framework or require you to learn yet another ML packaging API. Instead, it lets you leverage the large Python ecosystem by structuring your ML project in a [Pythonic-way](
https://docs.python-guide.org/writing/structure/). Whisk does the structuring while you focus on the data science.

Read more about our [beliefs](#beliefs).

## Getting Started

Start by creating a project. Begin a terminal session and run the commands below. _Note: We use __demo__ as the project name in the examples below. If you use a different project name, be sure to replace __demo__ with the name of your project._

```
$ pip install whisk
$ whisk create demo
$ cd demo
$ source venv/bin/activate
```

The commands above do the following:

* [Install the whisk package](https://whisk.readthedocs.io/en/latest/installation.html)
* [Create a project](https://whisk.readthedocs.io/en/latest/cli_reference.html#whisk-create) named "demo"
* [Generate the project directory structure](https://whisk.readthedocs.io/en/latest/project_structure.html)
* Activate the project's venv

__To try out all of the features, continue the [quick tour of whisk →](tour_of_whisk.html#try-the-sample-model).__

## Examples

The [whisk-ml](https://github.com/whisk-ml) GitHub org contains example whisk projects. Check out these examples and clone them locally. Since whisk makes reproducibility "just work", in most cases you simply need to run [`whisk setup`](https://whisk.readthedocs.io/en/latest/cli_reference.html#whisk-setup) to use the models generated by the projects. Here are few examples to start with:

* [Text Classification with Pytorch](#)
* [Image Classification with Tensorflow](https://github.com/whisk-ml/bike_image_classifier_tensorflow)
* Iris Classification with SKLearn (Coming soon)

## Beliefs

* **A Reproducible, collaborative project is a solved problem for classical software** - We don't need to re-invent the wheel for machine learning projects. Instead, we need guide rails to help data scientists structure projects without forcing them to also become software engineers.
* **A notebook is great for exploring, but not for production** - A data science notebook is where experimentation starts, but you can't create a reproducible, collaborative ML project with just a `*.ipynb` file.
* **Python already has a good package manager** - We don't need overly abstracted solutions to package a trained ML model. A properly structured ML project makes it easy to use _pip_ for packaging a model, making it easy for _anyone_ to benefit from your work.
* **Version control is a requirement** - You can't have a reproducible project if the code and training data isn't in version control.
* **Docker and Kubernetes are usually not needed** - when we [explicitly declare and isolate dependencies](https://12factor.net/dependencies), we don't need to rely on the implicit existence of packages installed in a Docker container. Docker also creates a slow development flow: repeatedly restarting Docker containers is far slower than doing the same in pure Python. Python already has solid native tools for this problem.
* **Optimize for debugging** - 90% of writing software is fixing bugs. It should be easy to debug your model logic locally. You should be able to search your error and find results, not sift through custom package source code.


## Contributing

Want to help build whisk? Check out our [contributing documentation](https://github.com/whisk-ml/whisk/blob/master/docs/contributing.md).

## Credits

This package was created with Cookiecutter and the `audreyr/cookiecutter-pypackage` project template. The project template is heavily inspired by [Cookiecutter Data Science](https://github.com/drivendata/cookiecutter-data-science).
