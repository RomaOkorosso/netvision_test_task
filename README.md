# Netvision test task

## Task description

[✅] Create FastAPI app with:

- [✅] POST /api/v1/text/new - create new text entry
- [✅] GET /api/v1/text/{uuid} - get text entry by uuid
- [✅] GET /api/v1/text/all - get all text entries
- [✅] DELETE /api/v1/text/{uuid} - delete text entry by uuid
- [✅] GET /api/v1/text/{count} - get text entries by count (from old to new)

[✅] Create client for this API with:

- [✅] Inserting 10-100 new rows
- [✅] Deleting 10 rows
- [✅] Run every 10 sec

[✅] Run everything in docker-compose

## Created with

- [Python 3.10](https://www.python.org/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Docker](https://www.docker.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)

## How to run

1. Clone this repo ```bash
   git clone https://github.com/RomaOkorosso/netvision_test_task.git```
2. Go to the project directory ```bash
   cd netvision_test_task```
3. Clone env file ```bash
   cp .env.example .env```
4. Make sure that your .env is good
5. Make sure that you have docker and docker-compose installed
6. Run ```bash
   docker-compose up```
7. Enjoy!

Logs are placed in `logs/`

## Docs

Go to `http://localhost:{APP_PORT}/api/v1/docs`