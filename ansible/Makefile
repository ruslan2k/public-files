SHELL := /bin/bash

redash:
	time ansible-playbook redash.yml -i hosts

default:
	ansible -i hosts -m ping all
