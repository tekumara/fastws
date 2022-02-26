# add additional targets here

# run app
run:
	uvicorn fastws.main:app --reload

# connect to websocket
ws:
	@echo "Enter any message to send a background email!"
	websocat ws://localhost:8000/ws/send-notification/awesome.io

include *.mk
