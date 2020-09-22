#-------------------------------------------------------------------------------
# Name:        Autorun
# Purpose:     Tool bots
#
# Author:      t3fox
#
# Created:     06/08/2020
# Copyright:   (c) t3fox 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import subprocess
import time
import shutil
import os

class BasicMain:

    def __init__(self,hhbo):
        self.totusr = hhbo

    def Autohhrun(self):

        print("..::Ejecutando::..")

        time.sleep(2)

        subprocess.call("cls",shell=True)

        for exi in range(1,self.totusr):

            thecommand = "py theUsr{}.py".format(exi)

            subprocess.call(thecommand,shell=True)

    def clloner(self):
        while True:

                MRS_PATH = str(os.getcwd())
                mrs_dir = "TheUsrs/"
                for n in range(1,self.totusr):

                    mr_file = "theUsr"
                    mrs_extend = ".py"
                    mr_num = n

                    #commit = False cloner
                    #dirBO = shutil.copy("theUsr.py","{}/{}{}{}{}".format(MRS_PATH,mrs_dir,mr_file,mr_num,mrs_extend))
                    print("\n\t----- Generando Nuevo_Usuario -----")
                    time.sleep(.5)

                print("\n\n----- Proceso Terminado -----\n\n")
                break




cant = int(input("Cantidad de usuarios: "))

builder = BasicMain(cant+1)
#builder.clloner()


option = input("Desea ejecutar: y/n: ")

if option == "y":
   builder.Autohhrun()
else:
    print("Proceso interrumpido")



