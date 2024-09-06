#Archivo: setup.py 

from setuptools import setup, find_packages 

setup(
        name = "model_devices", 
        versison="0.1.0", 
        packages=find_packages(), 
        install_requires=[
            "numpy",
            "matplotlib",
            ], 
        author = "Ovier ObregonH", 
        description="Libreira para modelar dispositivos electronicos", 
        long_description_content_type ="text/markdown", 
        url="https://github.com/"
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License", 
            "Operating System :: OS Independent", 
            ], 
        python_requieres='>=3.6', #version minima de python requerida 
        )
