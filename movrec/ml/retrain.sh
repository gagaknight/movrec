#!/bin/bash
while true ; 
do
	wget -O- "http://127.0.0.1:8000/retrain_model/"
	sleep 10
done
