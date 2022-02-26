# add additional targets here

# run app
run:
	uvicorn fasttask.main:app --reload

# connect to websocket
ws:
	@echo "Enter any message to start the background task"
	websocat ws://localhost:8000/ws/send-notification/awesome.io

include *.mk
