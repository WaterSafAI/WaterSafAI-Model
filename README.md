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
You can create a new virtual environment in PyCharm by opening the cloned repo as a PyCharm project and navigating to:

`Settings>Project>Python Interpreter` 

Then select:

`Add Interpreter>Add Local Interpreter`

Add the path to your local `python.exe` if PyCharm doesn't automatically detect it, and set the location path to 
`/WaterSafAI-Model/venv`.

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

# Flask API Model Wrapper

This application is containerized using Docker. Here are the steps to set up and run the application:

## Docker Setup

1. **Install Docker:** You can download Docker from [here](https://www.docker.com/products/docker-desktop). Follow the instructions for your specific operating system.

2. **Pull the PyTorch image:** Once Docker is installed, you can pull the PyTorch image using the following command:

    ```
    docker pull pytorch/pytorch
    ```

## Google Cloud Setup

Next, you need to install the Google Cloud SDK, which includes the gcloud command-line tool. To install the Google Cloud SDK, you need to follow these steps:

### For Windows:

1. Download the Interactive Installer:

    - Go to the [Google Cloud SDK webpage](https://cloud.google.com/sdk/docs/install).

    - Click on the “Install for Windows” button.

    - This will download the interactive installer.

2. Run the Installer:

    - Once downloaded, run the installer and follow the instructions.

    - During installation, it may ask you to log in to your Google Cloud account.

### For macOS and Linux:

1. Open the Terminal:

    - Open a terminal window.

2. Run the Installation Command:

    - Use the following curl command to install the SDK:

        ```
        curl https://sdk.cloud.google.com | bash
        ```

3. Restart Your Terminal:

    - Restart your terminal for the changes to take effect.

After installing the Google Cloud SDK, you need to authenticate with your Google Cloud account. Run the following command from the root directory and follow the prompts:

```
gcloud auth application-default login
```

## Building and Running the Docker Container

1. Build the Docker image:

    ```
    docker build -t flask-service .
    ```

2. Run the Docker container:

    ```
    docker run -p 4000:80 flask-service
    ```

## Making Requests to the Server

Once the server is running, you can make a `curl` request to the server:

```
curl -X POST http://localhost:4000/predict ^
-H "Content-Type: application/json" ^
-d "{\"ph\": 9.4, \"Hardness\": 145.8, \"Solids\": 13168.5, \"Chloramines\": 9.4, \"Sulfate\": 310.5, \"Conductivity\": 592.6, \"Organic_carbon\": 8.6, \"Trihalomethanes\": 77.5, \"Turbidity\": 3.87}"
```

## Google Cloud Deployments

To deploy the Dockerized application to Google Cloud, you can use Google Cloud Run. Here are the steps:

1. Build your Docker image using Cloud Build:

    ```
    gcloud builds submit --tag gcr.io/watersafai/flask-service
    ```
    
2. Deploy your image to Cloud Run:

    ```
    gcloud run deploy --image gcr.io/watersafai/flask-service --platform managed
    ```
