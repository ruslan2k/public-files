include ${HOME}/git/private/cloudant.cfg

URL:=https://${user}.cloudant.com
CURL:=curl --user ${user}:${pass}

default:
	@$(CURL) ${URL}
	@$(CURL) ${URL}/_all_dbs
	@$(CURL) ${URL}/test/_all_docs | jq .
	@$(CURL) ${URL}/test/document_id1 | jq .

add:
	@$(CURL) -X PUT ${URL}/${DB_NAME}/document_id1 \
	    -H 'Content-Type: application/json' -d '{"foo":{"bar":"baz"}}' | jq .

del:
	@$(CURL) -X DELETE ${URL}/${DB_NAME}/document_id1

#add2:
#	@$(CURL) -X POST ${URL}/${DB_NAME} \
#	    -H 'Content-Type: application/json' -d '{"foo":"bar"}' | jq .
