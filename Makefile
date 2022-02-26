# add additional targets here

# run app
run:
	uvicorn fasttask.main:app --reload

# send notification
send:
	curl -XPOST http://localhost:8000/send-notification/jordan@awesome.io

include *.mk
