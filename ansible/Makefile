SHELL := /bin/bash

redash:
	time ansible-playbook redash.yml -i hosts --ask-sudo-pass --check --diff

default:
	ansible -i hosts -m ping all
