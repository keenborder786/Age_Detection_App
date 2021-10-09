install:
	pip install -r requirements.txt 
lint:
	pylint --disable=R,C Main/Data_Module.py
	pylint --disable=R,C Main/inference_module.py
	pylint --disable=R,C Main/Train_Module.py
format:
	black Main/Data_Module.py
	black Main/inference_module.py
	black Main/inference_module.py