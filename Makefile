all_targets=adc_module/ tests/ deploy/

install:
	pip install .
	pip install ."[development]"
	pip install ."[micropython_deploy]"
	pip install ."[format]"
	pip install ."[lint]"
	pip install ."[test]"

lint:
	black $(all_targets)
	ruff check $(all_targets)
	mypy $(all_targets)

test:
	export PYTHONPATH=./adc_module; pytest tests/adc_module 

all: lint test

micro-cleanup-all:
	mpremote run deploy/cleanup.py

micro-common: 
	mpremote fs cp python_dummies/typing.py :typing.py 
	mpremote fs cp python_dummies/abc.py :abc.py 
	mpremote fs mkdir collections 
	mpremote fs cp python_dummies/collections/abc.py :collections/abc.py 

adc-module: micro-cleanup-all micro-common
	mpremote fs mkdir adc_module 
	mpremote fs cp adc_module/base.py :adc_module/base.py 
	mpremote fs cp adc_module/adc_module_logic.py :adc_module/adc_module_logic.py 
	mpremote fs cp adc_module/hardware.py :adc_module/hardware.py 
	mpremote fs cp adc_module/dft.py :adc_module/dft.py 
	mpremote fs cp adc_module/fft.py :adc_module/fft.py 
	mpremote fs cp adc_module/display.py :adc_module/display.py 
	
	mpremote fs cp adc_module/main.py :main.py 
	mpremote reset

 