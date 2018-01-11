start: venv
	venv/bin/python app.py

venv:
	virtualenv -p python3 venv
	venv/bin/pip install -r requirements.txt

test:
	venv/bin/python test.py
	sqlite3 examplpe.db .dump

doc: petstore-minimal.yaml
	pretty-swag -i $< -o docs/index.html
	cd docs && ../venv/bin/python -m http.server 8000

