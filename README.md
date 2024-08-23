# Create the virtual enviroment in Power Shell
python -m venv venv

# Active the virtual enviroment in Power Shell
source venv/bin/activate

# Python version of the project in Power Shell
Python 3.12.1

# Install poetry
pip install poetry

Run:
poetry lock
poetry install

# Install the dependicies
pip install -r requirements.txt

# Running the Script: 
poetry run recruitment

poetry run train n 

Note: where n is the number of training iterations