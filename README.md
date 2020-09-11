# create virtual environment and activate it
python3 -m venv my_virtual_environment
source my_virtual_environment/bin/activate
# within virtual environment, install dependencies:
pip3 install -r requirements.txt
#run api locally
python3 app.py --debug (can remove flag if desired.)
