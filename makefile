# Makefile

# Variables
SCRIPT = zip_script.sh

# Target rule
zip_folders:
	bash $(SCRIPT) $(VERSION)

.PHONY: zip_folders
