
.PHONY : all

all: rabbitadmin/client.py

rabbitadmin/client.py: api.json
	makerestapiclient -I 'from . import http' -i api.json -C -d http.HTTP -p api/ > rabbitadmin/client.py

clean:
	-rm rabbitadmin/client.py
