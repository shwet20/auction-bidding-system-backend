include .env
export

verbosity=1

help:
	@echo "Usage:"
	@echo " make help			-- display this help"
	@echo " make Install			-- creates database, install dependancies and migrates migrations"
	@echo " make test			-- run the tests and checks lint issues"
	@echo " make run			-- run server"
	@echo " make lint-fix			-- fixes the lint issues"
	@echo " make install-db		-- creates database if not exists (Only postgreSQL)"
	@echo " make install-django		-- migrates migrations"
	@echo " make install-pip		-- install dependancies"
	@echo " make generate-secret-key	-- generate secret key required for django"
	@echo " make create-app		-- create new django app/module"
	@echo " make check-deploy		-- review settings before deployment"

# Review settings before deployment
check-deploy:
	@python manage.py check --deploy

# Generate unique secret key for development
generate-secret-key:
	@python manage.py generate_secret_key

# Create database if it doesn't exist
install-db:
	if [ `psql -t -c "SELECT COUNT(1) FROM pg_catalog.pg_database WHERE datname = '${DB_NAME}'"` -eq 0 ]; then \
			psql  -c "CREATE DATABASE ${DB_NAME}"; \
	fi

# Install all required dependencies
install-pip:
	@pip install -r requirements.txt

# Run migration on database
install-django:
	@python manage.py migrate

# Install git hooks
# https://pre-commit.com/ for more details
install-hooks:
	@pre-commit install

# Install dependancies and run migrations
install: install-pip install-django install-hooks

# Start application
run:
	@python manage.py runserver 0.0.0.0:${PORT}

# Run tests
test:
	@flake8 .
	@coverage run  --source=$(path) manage.py test --keepdb --verbosity=$(verbosity) $(path)
	@coverage report -m

# Fix linting issues
lint-fix:
	@autopep8 ./ --exclude="*/migrations/*.py"

# Command to run new django app/module
create-app:
	@python manage.py create_app --name=${name}

#Command to create super user
create-superuser:
	@python manage.py createsuperuser