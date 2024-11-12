#!/bin/bash
cd /home/site/wwwroot
python -m pip install -r requirements.txt
python -m streamlit run fees_travel_calculator_app.py --server.port 8000 --server.address 0.0.0.0