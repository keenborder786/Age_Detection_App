install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt --user
lint:
	pylint --disable=R,C Main/Data_Module.py
	pylint --disable=R,C Main/inference_module.py
	pylint --disable=R,C Main/Train_Module.py
format:
	black *.py