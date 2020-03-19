curl --location --request POST 'http://localhost:5000/nginx' \
--header 'Content-Type: application/json' \
--data-raw '{
	"project_name":"{project_name}"
}'