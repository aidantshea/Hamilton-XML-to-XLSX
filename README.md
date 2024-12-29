# Plate-Converter-Application
This repository contains the codebase for the PlateConverterApp, a windows desktop application that transforms .xml output data from the Hamilton MicroLab STAR liquid handler into a useable .csv import file for the 7500 ThermoFisher Real-Time qPCR platform. 

----------------------------------------------------------------------------------------------------------------------------------------------------------------------

dependencies:			    PySide6
                            PyInstaller
                            openpyxl

package manager: 		    MiniForge3

environment name:		    PlateConverterEnv

environment command:		conda create -n PlateConverterEnv PySide6 PyInstaller openpyxl


PyInstaller command:
PyInstaller --windowed application.py --add-data "template.xlsx:." --add-data "methods.py:." --add-data "readme.txt:." --hidden-import openpyxl.cell._writer -y