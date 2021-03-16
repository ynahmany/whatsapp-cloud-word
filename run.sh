#! /bin/bash
docker build -t whatsapp-cloud:latest .

docker run -d -p 5000:5000 whatsapp-cloud