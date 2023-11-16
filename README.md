# WaterSafAI Water Quality Prediction Model

This is the GitHub Repo for the AI data model that the WaterSafAI mobile application uses in order to make residential
water quality predictions and recommendations. Built using `PyTorch`.

## Development Environment
### Python Version
Project was set up in a development environment using `Python 3.9`, but it should work with newer versions of python as well.

Download Python: https://www.python.org/downloads/

### Environment Managers
In order to reduce dependency conflicts, development on this model should be done in virtual python environment using `venv`
or `Anaconda`. Initial project setup was done using `venv` so it is recommended to follow these setup steps:

Anaconda (https://www.anaconda.com/download) is downloaded separately, but venv is included with Python installations by default.

### VS Code
Install the `Python Environment Manager` extension which allows you to create and manage virtual python environments. Use
the extension to create a new environment using the command palette (`ctrl+shift+P`) and select the command 
`Python: Create Environment...`. You can name it whatever you want, but we will call it `watersafai`.

Open a Terminal in VS Code with the new virtual environment active. This will let you install necessary packages using
`pip` that will only be applied to the virtual environment, and let you run the program isolated from unnecessary dependencies.
Make sure your virtual environment is active

### PyCharm
You can create a new virtual environment in PyCharm by opening `WaterSafeAI-App/model` as a PyCharm project and navigating to:

`Settings>Project>Python Interpreter` 

Then select:

`Add Interpreter>Add Local Interpreter`

Add the path to your local `python.exe` if PyCharm doesn't automatically detect it, and set the location path to `/model/venv`.

This will place the new virtual environment in the project directory, and it can be used as a run configuration.

### Installing PyTorch
WaterSafAI's AI model is built with `PyTorch`, and while most of the packages used for this project can be installed with
`pip` as outlined below, your PyTorch installation will depend on the machine you are developing with. 

To install PyTorch locally, go to https://pytorch.org/get-started/locally/ and run the provided command in a terminal 
running your `watersafai` virtual environment. The download site will autodetect the best settings for your system 
configuration.

### pip
All package dependencies are included in `requirements.txt`

Install necessary packages using `pip` (included in Python installations) with the command:

```
pip install -r requirements.txt
```

When contributing to the repo, make sure any additional packages you've installed locally are added to `requirements.txt`
in the format:
```
<package>==<version>
```

## Usage

To execute a training run for the model, open the cloned repo directory in your terminal. If you are using a virtual 
environment make sure it's active in that terminal.

Run

``` 
python main.py
```
