# Nombre del ambiente virtual de Python
VENV_NAME = .venv

# Comando para desactivar el ambiente virtual
DEACTIVATE_ENV = deactivate

# Objetivo predeterminado
generate: activate_venv generate_code

init: create_venv install_requirements

create_venv:
	@echo "Creando ambiente virtual..."
	@python3 -m venv $(VENV_NAME)

install_requirements:
	@echo "Instalando requerimientos..."
	@pip install -r requirements.txt

# Activar el ambiente virtual
# if terminal is zsh, use "source" instead of "."
# if terminal is bash, use "." instead of "source"
# if terminal is fish, use . .venv/bin/activate.fish
activate_venv:
	@echo "Activando ambiente virtual..."
	@if [ "/usr/local/bin/fish" = "$(SHELL)" ]; then \
		. $(VENV_NAME)/bin/activate.fish; \
	else \
		. $(VENV_NAME)/bin/activate; \
	fi

# Generar el código usando ANTLR
generate_code:
	@echo "Generando código con ANTLR..."
	@antlr4 -v 4.13.0 -Dlanguage=Python3 -visitor -no-listener lenguaje.g4 -o generatedcode

