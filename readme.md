## PYTHON FLASK API BASE
# Easy Standup with Docker

# Local setup Instructions

1. Open Terminal
2. Execute the following commands:
    - python -m venv venv
    - .\venv\Scripts\activate
    - pip install flask flask-restful

# Docker setup Instructions

* Make sure you have the latest Docker version installed on your local machine

1. Open Terminal
2. Execute the following commands:
    - docker build -t <name of image> .
    - docker run -p <Your Machines Port>:5000 pythonapi
3. Navigate to: localhost:<Your Machines Port>

