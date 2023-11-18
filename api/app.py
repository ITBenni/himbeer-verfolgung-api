from connexion import FlaskApp, AsyncApp
from connexion.middleware import MiddlewarePosition
from starlette.middleware.cors import CORSMiddleware


app = AsyncApp(__name__, specification_dir="./")
app.add_api("swagger.yml")


# Add %&*$#*# CORS headers
app.add_middleware(
	CORSMiddleware,
	position=MiddlewarePosition.BEFORE_ROUTING,
	allow_origins=["*"],
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"],
	expose_headers=["*"],
	max_age=3600
)

if __name__ == '__main__':
	app.run(port=8000)