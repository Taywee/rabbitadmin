
.PHONY : all

all: rabbitadmin/__init__.py

rabbitadmin/__init__.py: api.json
	makerestapiclient -I 'from . import http' -i api.json -C --indent '    ' -d http.HTTP -p api/ > rabbitadmin/__init__.py

clean:
	-rm rabbitadmin/__init__.py
