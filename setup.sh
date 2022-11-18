#!/bin/bash
python3 -m venv weather_pipeline_venv 
source ./weather_pipeline_venv/bin/activate 
pip3 install -r requirements.txt
$2