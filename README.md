# PyPDFToolkit: PDF Organization and Conversion Tools

## Overview

PyPDFToolkit is a collection of Python scripts for organizing and manipulating PDF files. It provides functionalities such as merging multiple PDFs, compressing PDFs, and converting images to PDFs. The script utilizes various libraries like Tkinter, PyPDF2, Pillow, img2pdf, and reportlab to achieve these tasks.

## Features

### PDF Merger
The PDF Merger tool allows you to select multiple PDF files and merge them into a single PDF document. The merged PDF is saved to the location you specify.

### PDF Compressor
The PDF Compressor tool enables you to select PDF files and compress them, reducing their file size. The compressed PDFs are saved to the destination you choose.

### Image to PDF Converter
The Image to PDF Converter tool lets you select multiple image files (in supported formats) and convert them into a single PDF document. The resulting PDF is created with the images positioned and scaled appropriately.

## Installation

1. Clone or download this repository to your local machine.
2. Open a terminal or command prompt.
3. Navigate to the project directory.
4. Run the following command to install the required packages:
```
pip install PyPDF2 Pillow img2pdf reportlab ttkbootstrap
```

## Usage
1. Clone the repo
```
  git clone https://github.com/kourdroid/PyPDFToolkit.git
```
2. Enter the Repository:
```
   cd PyPDFToolkit  
```
3. Run the script using Python:
```
  python pdforganizer.py 
```
Please note that this script requires Python 3.x to run.

## How to Use

1. Choose the desired tool from the main menu: PDF Merger, PDF Compressor, or Image to PDF Converter.
2. Follow the prompts to select input files and specify output locations.
3. The progress bar will show the status of the operation.
4. Once completed, the output file will be available at the specified location.

## License

This project is licensed under the terms of the MIT License. See the [LICENSE](LICENSE) file for details.

**Disclaimer:** This script is intended for personal use and learning purposes. Always make sure you have the necessary permissions to manipulate files before using this tool on them.

