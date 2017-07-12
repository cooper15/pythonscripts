#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
from time import sleep
import logging

LS_COMMAND = "ls | grep "

# Filter definitions
# ---------------------------------------------------------------------------------------
TUPLE_DOCUMENTS_FILTER = (".*.pdf.*", ".*.doc.*", ".*.docx.*", ".*.xls.*", ".*.xlsx.*")
TUPLE_IMAGE_FILTERS = (".*jpg.*", ".*.png.*")
# ---------------------------------------------------------------------------------------

# Final paths
# ---------------------------------------------------------------------------------------
ORIGIN_PATH = " ~/Descargas/"
PICTURES_FINAL_PATH = " ~/Imágenes/"
COMPROBANTES_FINAL_PATH = " ~/Dropbox/Comprobantes_de_Pago_electronico/"
DOCUMENTS_FINAL_PATH =" ~/Documentos"
# ---------------------------------------------------------------------------------------

def get_pictures():
    pictures_name = []
    for index in range(0, len(TUPLE_IMAGE_FILTERS)):
        for line in os.popen(LS_COMMAND + TUPLE_IMAGE_FILTERS[index], 'r', 1):
            pictures_name.append(line.strip())
    return pictures_name


def get_comprobantes():
    documents_name = []
    for line in os.popen(LS_COMMAND + "Comprobante", 'r', 1):
        documents_name.append(line.strip())
    return documents_name


def get_documents():
    documents_name = []
    for index in range(0, len(TUPLE_IMAGE_FILTERS)):
        for line in os.popen(LS_COMMAND + TUPLE_DOCUMENTS_FILTER[index], 'r', 1):
            documents_name.append(line.strip())
    return documents_name

if __name__ == '__main__':
    logging.basicConfig(
        format='%(asctime)s %(message)s', filename="secretary_mv.log", level=logging.DEBUG)
    logging.debug("starting")
    while True:
        for picture in get_pictures():
            os.system("mv " + "'" + picture + "'" + PICTURES_FINAL_PATH)
            logging.debug("mv " + picture + " to " + PICTURES_FINAL_PATH)
        for comprobante in get_comprobantes():
            os.system("mv " + "'" + comprobante + "'" + COMPROBANTES_FINAL_PATH)
            logging.debug("mv " + comprobante + " to " + COMPROBANTES_FINAL_PATH)
        for document in get_documents():
            os.system("mv " + "'" + document + "'" + DOCUMENTS_FINAL_PATH)
            logging.debug("mv " + document + " to " + DOCUMENTS_FINAL_PATH)
        sleep(30)
