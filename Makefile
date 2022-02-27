# add additional targets here

# run app
run:
	uvicorn fastws.main:app --reload

# connect to websocket
ws:
	@echo "Enter an username to send a email!"
	websocat ws://localhost:8000/ws/send-notification/awesome.io

# start vite dev server
start:
	npm start

# build production app in dist/
build:
	npm run build

include *.mk
