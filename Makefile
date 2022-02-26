# add additional targets here

# run app
run:
	uvicorn fasttask.main:app --reload

# send notification
send:
	curl -XPOST http://localhost:8000/send-notification/one@awesome.io
	sleep 2
	curl -XPOST http://localhost:8000/send-notification/two@awesome.io
	curl -XPOST http://localhost:8000/send-notification/three@awesome.io
	sleep 2
	curl -XPOST http://localhost:8000/send-notification/four@awesome.io


include *.mk
