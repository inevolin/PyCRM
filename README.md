# PyCRM

## Intro
This repository is dedicated to solving various (complex) problems using software, primarily the Python programming language. More specifically  business solutions to Customer Relationship Management (CRM), Client and Data Management. Some problems can be solved or automated using simple code snippets, while more complex issues involve machine learning (A.I.) approaches.

Remember that well-organized businesses face less issues and have a higher productivity, especially when it comes to client, document and data management. It is essential to have structure and discipline within your organization, no matter your role in that company.

## Requirements
You should use a Linux system with Python 3.6+ with pip.
Other operating systems should work as well, but you'll need to manually figure out how to install 3rd-party dependencies.

## Document Management
It's important to properly manage your digital documents such as scans, pictures, invoices, and on. Some businesses use CRM software for storing and labeling their client/project related files.

### OCR
It's not always easy to manage files, some businesses simply dump all files into a single folder but never clean it up. And when you have a high flux of files coming in on a daily basis you may feel overwhelmed. Or you may already find yourself in a big disorganized mess and feel discouraged. Fortunately technology can help us. OCR stands for Optical Character Recognition, it's a machine learning discipline focusing on extracting text from images/pictures. 

Regular text-based files can easily be read and parsed. But the OCR library allows us to easily and quickly parse text from image, pdf and docx files. The text/keywords obtained from these files can be used for labeling/processing files automatically.

Suppose you have hundreds of files, and most of these are copies of passports, contracts and invoices. Some are images were taken by phone, some were scanned images, some are PDF files containing images, some are text-based PDF files. The demo screenshots below illustrate how we can extract text/keywords from these kinds of documents.

#### OCR in action:

![OCR passport](https://raw.githubusercontent.com/healzer/PyCRM/master/git_assets/ocr_demo.png)

![OCR invoice pdf image](https://raw.githubusercontent.com/healzer/PyCRM/master/git_assets/ocr_demo2.png)

Using the extracted text/keywords we can process these files according to our own business rules, such as rename/copy/move/backup; but we can also send/upload these files to some other pipeline for further processing. Keep in mind that OCR is pretty good but it's not perfect, it works best when images are clear and don't contain strange characters. Most languages are supported.

#### OCR usage

Here's a basic way of using the OCR library (`ocr.py`) in your own workflow.
```python
import ocr

your_file = './demo_files/doc1.pdf'
text = ocr.process(your_file)

# business rule
if 'CONTRACT' in text:
  ...
else:
  ...
```

Have a look inside the `demo_files` directory for more demo files.

#### OCR installation

To use the OCR library we have to install several dependencies:
```
apt-get install python-dev libxml2-dev libxslt1-dev antiword unrtf poppler-utils pstotext tesseract-ocr flac ffmpeg lame libmad0 libsox-fmt-mp3 sox libjpeg-dev swig libpulse-dev libmagickwand-dev

python3 -m pip install pytesseract
python3 -m pip install wand
python3 -m pip install textract
python3 -m pip install pillow
```

Finally we need to adjust a setting in the file `/etc/ImageMagick-6/policy.xml`. Near the bottom you will find the line:
```<policy domain="coder" rights="none" pattern="PDF" />```
change this to:
```<policy domain="coder" rights="read" pattern="PDF" />```
now save and close the file.

Now you can test the installation by running:
```python3 ocr_tests.py```
This will run several OCR default tests, which should all complete successfully, if anything went wrong during the installation you should see some error messages.

# Support
For questions, problems and inquiries reach out to Ilya Nevolin at ilja.nevolin@gmail.com 
