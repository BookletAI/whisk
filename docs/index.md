# whisk documentation

__whisk is an open-source ML project framework that make makes collaboration, reproducibility, and deployment "just work".__ It combines a suite of lightweight tools with a logical and flexible project structure. Release your model to the world without a software engineer.

Whisk doesn't lock you into a particular ML framework or require you to learn yet another ML packaging API. Instead, it lets you leverage the large Python ecosystem by structuring your ML project in a [Pythonic-way](
https://docs.python-guide.org/writing/structure/). Whisk does the structuring while you focus on the data science.

Read more about our [beliefs](#beliefs).

## A quick tour of whisk

The best way to experience whisk is by creating your first project. The short self-guided tour below shows the power of whisk.

_We use __demo__ as the project name in the examples below. If you use a different project name, be sure to replace __demo__ with the name of your project._

### Create a project

Start by creating a project. Begin a terminal session and run the commands below:

```
$ pip install whisk
$ whisk create demo
$ cd demo
$ source venv/bin/activate
```

This installs the whisk package, creates the project, and activates the project's venv.

### Try the sample model

The project contains a simple model stub that returns the length of each inner list within a 2D array. The model is saved to the disk using pickle. We can use the model stub to demonstrate the full capabilities of a whisk project.

Since a whisk project uses a standard Python project code structure, there are multiple ways to invoke the model.

#### From Python code

The model code resides in the `src/demo` directory of the project. The source code is installed as an editable Python package, so you can run the model from the Python console or from within a notebook cell:

```py
from demo.models.model import Model
model = Model()
model.predict([[0,1],[2,3]])
```

The `Model` class loads the model from disk and `Model.predict` passes the data into the model.

#### From the command line

The project is pre-wired with [Click](https://click.palletsprojects.com/en/7.x/), a Python package for creating beautiful command line interfaces. Invoke the model right from the terminal:

```
$ demo predict [[0,1],[2,3]]
[2, 2]
```

#### From the Flask App

There's a ready-to-go Flask web service in the `app/` directory. Start the web service:

```
$ whisk app start
```

Make a request in another terminal session:

```
$ curl --location --request POST 'http://localhost:5000/predict' \
--header 'Content-Type: application/json' \
--data-raw '{"data":[[0, 1], [2, 3]]}'
```

### Sharing the model

You can let others use your model by releasing a Python package and deploying a web service.

#### Release a Python Package for your model

Create a **Python package** containing your model. This lets anyone use your model that has Python installed on their computer:

```
$ whisk package dist
Python Package created in /Users/dlite/projects/whisk_examples/demo/dist:
demo-0.1.0.tar.gz

$ pip install dist/demo-0.1.0.tar.gz
```

After installing the package, another user can invoke the model via the CLI or by importing the `demo` module like we did earlier.

#### Deploy a web service

You can deploy the model inference web service to Heroku ([a free account](https://signup.heroku.com/) works fine with this demo):

```
$ whisk app create demo-[INSERT YOUR NAME]
```

### What next?

#### Open the example notebook


The project includes an interactive notebook that shows how to save your trained model to disk, use the saved model to generate predictions, how to load Python functions and classes from the project's `src` directory, and more. It's the guide rails for your own ML project.

```
$ jupyter-notebook notebooks/getting_started.ipynb
```

#### Explore a real whisk project

The [whisk-ml](https://github.com/whisk-ml) GitHub org contains example whisk projects. Checkout these examples and clone them locally - since whisk makes reproducibility "just work", in most cases you simply need to run `whisk setup` to begin trying the models generated by the projects.

## Documentation

```eval_rst
.. toctree::
   :maxdepth: 2

   key_concepts
   installation
   usage
   modules
   changelog
   contributing
```

## Beliefs

Most ML framework approaches start with a shaky foundation. Rather than building off software engineering best practices for structuring your work, they encourage quick hacks that result in ML projects that are hard to debug, collaborate on, reproduce, and deploy. The beliefs below inspired us to create whisk:

* **A Reproducible, collaborative project is a solved problem for classical software** - We don't need to re-invent the wheel for machine learning projects. Instead, we need guide rails to help data scientists structure projects without forcing them to also become software engineers.
* **A notebook is great for exploring, but not for production** - A data science notebook is where experimentation starts, but you can't create a reproducible, collaborative ML project with just a `*.ipynb` file.
* **Optimize for debugging** - 90% of writing software is fixing bugs. It should be fast and easy to debug your model logic locally. You should be able to search your error and find results, not sift through custom package source code or stop and restart Docker containers.
* **Python already has a good package manager** - We don't need overly abstracted solutions to package a trained ML model. A properly structured ML project lets you distribute the model via `pip`, making it easy for _anyone_ to benefit from your work.
* **Version control is a requirement** - You can't have a reproducible project if the code and training data isn't in version control.
* **Docker is an unsteady foundation** - when we [explicitly declare and isolate dependencies](https://12factor.net/dependencies), we don't need to rely on the implicit existence of packages installed in a Docker container. Python has solid native tools for dependency management.
* **Kubernetes is overkill** - very few web applications require the complexity of a container-orchestration system. Your deployed model is no different. Most models can run on boring, reliable technology.

```eval_rst
Indices and tables
==================
* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
```