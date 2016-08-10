
.PHONY : all test

all: rabbitadmin/client.py

rabbitadmin/client.py: api.json
	makerestapiclient -I 'from . import http' -i api.json -C -d http.HTTP -p api/ > rabbitadmin/client.py

test: rabbitadmin/client.py
	PYTHONPATH="$$(pwd)" ./tests/test.py

clean:
	-rm rabbitadmin/client.py
