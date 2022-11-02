from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from core.config import settings
from db.session import engine   #new
from db.base import Base  #new


def configure_static(app):
    app.mount("/static", StaticFiles(directory="static"), name="static")


def create_tables():
	print("create_tables")
	Base.metadata.create_all(bind=engine)

	
def start_application():
	app = FastAPI(title=settings.PROJECT_NAME,version=settings.PROJECT_VERSION)
	configure_static(app)
	create_tables()       #new
	return app

app = start_application()

