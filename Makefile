deploy:
	for f in *.py; do echo "ampy put $$f"; done

run:
	ampy run main.py
