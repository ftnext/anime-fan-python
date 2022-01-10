.PHONY: all

all: convert runserver

convert:
	@python3 convert.py ainouta_watch_date.txt commits_ainouta.json

runserver:
	@echo "🏃‍♂️ Go http://localhost:8000/show_commits.html"
	@python3 -m http.server 8000
