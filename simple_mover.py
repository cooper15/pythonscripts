"""This script move documents to its right folder in the system"""
import subprocess
import logging
from os import system
from time import sleep


class MoveDocuments(object):
    logging.basicConfig(
        format='%(asctime)s %(message)s', filename="/home/cooper15/.scripts/secretary2_mv.log", level=logging.DEBUG)
    logging.debug("starting")

    @staticmethod
    def move_it(document_type, file_destination):
        """Find all kind of documents and move them to documents folder"""
        args = ["ls ~/Descargas | grep -i {}".format(document_type)]
        try:
            process = subprocess.Popen(args, stdout=subprocess.PIPE, shell=True)
            files = process.communicate()[0].strip().split()
            for file in files:
                file = file.decode()
                system("mv ~/Descargas/'{}'".format(file) + " " + file_destination)
                logging.debug("mv {}".format(file) + " to " + file_destination)
            return "Everything it's ok!!"
        except Exception as ex:
            logging.error(ex)
            return "Something went wrong"


if __name__ == '__main__':
    md = MoveDocuments()
    while True:
        md.move_it('comprobante', '~/ownCloud/Comprobantes_de_Pago_electronico')
        # md.move_it('.doc', '~/Documentos')
        # md.move_it('.pdf', '~/Documentos')
        # md.move_it('.xls', '~/Documentos')
        sleep(15)
