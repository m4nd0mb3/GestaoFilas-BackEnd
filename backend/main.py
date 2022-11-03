from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from apis.base import api_router
from core.config import settings
from db.session import engine   
from db.base import Base  

def include_router(app):   
	app.include_router(api_router, prefix=settings.API_V1_STR) 

def configure_static(app):
    app.mount("/static", StaticFiles(directory="static"), name="static")


def create_tables():
	print("create_tables")
	Base.metadata.create_all(bind=engine)

	
def start_application():
	origins = ['*']
	app = FastAPI(title=settings.PROJECT_NAME,version=settings.PROJECT_VERSION, description=settings.PROJECT_DESCRIPTION)
	app.add_middleware(
		CORSMiddleware,
		allow_origins = origins,
		allow_credentials = True,
		allow_methods = ['*'],
		allow_headers = ['*'],
	)
	configure_static(app)
	create_tables()       #new
	include_router(app)
	return app

app = start_application()
if __name__ == '__main__':
	import uvicorn
	uvicorn.run('main:app', host='0.0.0.0', port=8000,
				log_level='info', reload=True)

