# **random-data-generator**
This project is application for random data generation.
It was created using following technilogies:
- Python
- pandas, numpy [data transformation]
- Flask [web application]
- SQL Alchemy [Object Relational Mapper]

## How to run?
**Python** is required for this repository. 
To download and install Python, please follow this link: [python.org](https://www.python.org/).

In order to run application please follow steps below:

1. Download repository from GitHub and save in *random-data-generator* directory

2. Open terminal and go to _.../random-data-generator directory.

3. Create virtual environment with command `python -m venv venv`

4. Activate newly created virtual environment with a command:
   - `source venv/bin/activate` for Linux and macOS
   - `venv\Scripts\activate` for Windows
   
5. After creating and activating virtual environment, install all useful packages using pip
	- `pip install -r requirements.txt`

6. Run application with command `flask run`