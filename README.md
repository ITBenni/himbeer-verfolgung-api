<div align="center">

# <img src="docs/raspberry-pi.svg" style="height: 1em; aspect-ratio: 1/1; " aria-hidden="true"> Himbeer Verfolgung

A simple API for a RFID demo using Python

<br/>

</div>


## 💡 About The Project

This is a very simplistic project to demonstrate the possibilities of RFID technology.
It uses [Flask](https://flask.palletsprojects.com/en/3.0.x/), [Swagger](https://swagger.io/docs/specification/about/) and [Connexion](https://connexion.readthedocs.io/en/stable/) to create a RESTful API to track the movement of RFID tags. 

It is intended to be used in the lecture "Soziotechnische Studien: Container, Paletten, Verpackungen" taught by Prof. Dr. Martin Binder at [PH-Weingarten](https://technik.ph-weingarten.de/das-fach/das-fach/).

The project should be used in conjunction with this [frontend](https://github.com/ITBenni/himbeer-verfolgung-frontend) and this [RFID reader](https://github.com/ITBenni/himbeer-verfolgung-rfid). 


## 🧭 Getting Started

To get a local copy up and running follow these steps.

### Installation

1. Clone this repository

	```bash
	https://github.com/ITBenni/himbeer-verfolgung-api.git && cd himbeer-verfolgung-api
	```

2. Create and activate a virtual environment to make handling python dependencies less of a mess. 

	```bash
	python -m venv venv 
	source venv/bin/activate
	```

2. Install the project's dependencies

	```bash
	pip install -r requirements.txt
	```

## 🧑‍💻 Developing

The entrypoint to the application is located in [api/app.py](api/app.py). 
You can run the app with a regular python interpreter, or the development environment of your choice: 

```bash
python3 api/app.py
```

You can see the Swagger documentation of the API on [http://127.0.0.1:8000/api/ui/](http://127.0.0.1:8000/api/ui/). 


## 📦 Building

To create a deployable version of the project use the [Dockerfile](Dockerfile) and create a container:

```bash
docker build -t himbeer-verfolgung-api . 
docker run -d -p 8000:8000 himbeer-verfolgung-api
```

This is just a demo and not intended to run in a production environment! 


## 🤝 Contributing

Any contributions are welcome :)
If you find any errors or if you have feedback, please open an [issue on Github](https://github.com/ITBenni/himbeer-verfolgung-api/issues).


## 📜 License

Distributed under the MIT License. See [LICENSE](LICENSE) for more information.


## 🙏 Acknowledgments

This project stands on the shoulders of giants. Those are: 

- [Philipp Acsany's original post on Real Python](https://realpython.com/flask-connexion-rest-api/)

Without these amazing people this project would't have been possible. 