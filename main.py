import http.client
import mimetypes
import json
import os

auth0_token = os.getenv("AUTH0_TOKEN")
client_id = os.getenv("CLIENT_ID")
client_host = os.getenv("CLIENT_HOST")
web_origin_domain = os.getenv("WEB_ORIGIN_DOMAIN")
action_type = os.getenv("ACTION_TYPE")

conn = http.client.HTTPSConnection(client_host)
payload = ""

headers = {
    "Authorization": "Bearer " + auth0_token,
    "Content-Type": "application/json"
}

conn.request("GET", "/api/v2/clients/" + client_id, payload, headers)
res = conn.getresponse()

data = res.read()
data = data.decode("utf-8")
data = json.loads(data)
data = set(data["web_origins"])


if action_type == "add":
    data.add(web_origin_domain)
else:
    data.add(web_origin_domain)
    data.remove(web_origin_domain)

payload = json.dumps({"web_origins": list(data)})

print(payload)

conn.request("PATCH", "/api/v2/clients/" + client_id, payload, headers)
res = conn.getresponse()
