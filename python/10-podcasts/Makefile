new: venv
	venv/bin/python new.py
	sync

venv:
	virtualenv -p python3 venv
	venv/bin/pip install -r requirements.txt

update:
	wget -O Makefile https://raw.githubusercontent.com/ruslan2k/public-files/master/python/10-download/Makefile
	wget -O download.py https://raw.githubusercontent.com/ruslan2k/public-files/master/python/10-download/download.py
	$(MAKE) download

download:
	python download.py
	sync
