SHELL:=/bin/bash

redash:
	time ansible-playbook redash.yml -i hosts --diff

redash_prod:
	time ansible-playbook redash.yml -i hosts --ask-sudo-pass \
	    --diff --check

default:
	ansible -i hosts -m ping all
