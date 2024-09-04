# Archivo: setup.py

from setuptools import setup, find_packages

setup(
    name="model_device",  # Nombre del paquete
    version="0.1.0",      # Versión del paquete
    packages=find_packages(),  # Encuentra automáticamente los paquetes en la carpeta
    install_requires=[
        "numpy",
        "matplotlib",
    ],  # Dependencias necesarias
    author="Tu Nombre",
    description="Librería para modelar dispositivos electrónicos",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/tuusuario/proyecto_modelo_diodo",  # Cambia esto si subes a GitHub
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # Versión mínima de Python requerida
)
