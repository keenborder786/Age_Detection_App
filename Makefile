install:
	pip install -r requirements.txt 
lint:
	pylint Main
format:
	black Main/Data_Module.py
	black Main/inference_module.py
	black Main/inference_module.py