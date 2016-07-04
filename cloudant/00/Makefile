include /dev/shm//pass

URL:=https://${user}.cloudant.com

default:
		@curl  --user ${user}:${pass}  https://.cloudant.com/
		@curl  --user ${user}:${pass}  https://.cloudant.com/_all_dbs
		@curl -s --user ${user}:${pass}  https://.cloudant.com/test/_all_docs | jq
		@curl -X POST ${URL}/${DB_NAME} -H 'Content-Type : application/json' -d '{"foo":"bar"}' | jq
