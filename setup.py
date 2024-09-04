# Archivo: setup.py 
from setuptools import setup, find_packages 

setup(
        name = 'model_device',      #Nombre del paquete 
        version = '0.1.0',          # Version dle paquete 
        packages = find_packages()  # Encuentra automaticamente los paquetes en la carpeta 
        install_requieres = [
            "numpy",
            "matplotlib",
            ],
        author = "Ovier ObregonH", 
        description = "Libreria para modelar fisicamente dispositivoss electronicos", 
        long_description=open("README.md").read()
        long_description_content_type = "text/markdown", 
        url="https://github.com/ovier-oh/lib-model-device-0.1v",
        classifiers = [
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
            ],
            python_requires='>=3.6', #Version minima de python
        )
