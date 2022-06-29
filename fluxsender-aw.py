#Script made by Benji   

import os
import time
import shutil
import subprocess
import pyautogui

#LOGO

def logoaw():


    print("""

               ___    _  __         __              _      __             
              / _ |  / |/ / ___ _  / / ___   ___ _ | | /| / / ___ _  __ __
             / __ | /    / / _ `/ / / / _ \ / _ `/ | |/ |/ / / _ `/ / // /
            /_/ |_|/_/|_/  \_,_/ /_/  \___/ \_, /  |__/|__/  \_,_/  \_, / 
                                           /___/                   /___/  

                                FLUXSENDER - Made by Benji 
\n\n
""")









#Variables

yes = {'yes', 'y', 'Y', 'YES'}
no = {'no', 'n', 'N', 'NO'}

masternditxt = "/home/analogway/Bureau/MASTER-COPY/master-global.ini"


#Functions

def clearop():
    os.system('clear')

def main():

    clearop()

    logoaw()
   

    global nbrflux


    nbrflux = int(input("Combien de flux vidéos souhaitez vous ? \n\n >> "))
    
    if nbrflux > 0:
        print("ok")
        clearop()
        launchflux()
    if nbrflux < 1:  
        print("Erreur !")
        time.sleep(1)
        return main()

    
    

def launchflux():
    clearop()

    logoaw()

    typeresolutionask = int(input("Quelle type de résolution souhaitez vous ? \n\n -- FULL HD -- \n\n 1 - 1920x1080 - 30 FPS \n 2 - 1920x1080 - 60 FPS \n\n -- 4K (Peut causer des bugs/Crash d'OBS) -- \n\n 3 - 3840x2160 - 30 FPS \n 4 - 3840x2160 - 60 FPS \n\n >> "))
    if typeresolutionask is 1:
        print("Changement de la résolution pour de la FULL HD 30 FPS")
        resolutionmastertxt = open("/home/analogway/Bureau/MASTER-COPY/master-basic.txt", "w")
        resolutionmastertxt.write("""[General]
Name=Sans nom

[Video]
BaseCX=1920
BaseCY=1080
OutputCX=1920
OutputCY=1080
ScaleType=lanczos
FPSType=0
FPSCommon=30

[Panels]
CookieId=2250AF64FAA0208F

[Output]
Mode=Simple

[SimpleOutput]
VBitrate=5500

[AdvOut]
TrackIndex=1
RecType=Standard
RecTracks=1
FLVTrack=1
FFOutputToFile=true
FFFormat=
FFFormatMimeType=
FFVEncoderId=0
FFVEncoder=
FFAEncoderId=0
FFAEncoder=
FFAudioMixes=1

[WebsocketAPI]
ServerEnabled=false
ServerPort=4444
LockToIPv4=false
DebugEnabled=false
AlertsEnabled=true
AuthRequired=false
AuthSecret=KNWnlEjudME3icDdtuPML4KIC34AFVg574lAhMI5sgc=
AuthSalt=QgBrvFzzjy3k7fj9D+osqDlAk/PkzT8v3BB4jShmgao=
         """)
        resolutionmastertxt.close()   
        time.sleep(1)
        print("Changement de la résolution en cours...")
        srcresolution = r'/home/analogway/Bureau/MASTER-COPY/master-basic.txt'
        destresolution = r'/home/analogway/.config/obs-studio/basic/profiles/Sans nom/basic.ini' 
        shutil.copyfile(srcresolution, destresolution)
        print("Changement de la résolution terminé !")

    if typeresolutionask is 2:
        print("Changement de la résolution pour de la FULL HD 60 FPS")
        resolutionmastertxt = open("/home/analogway/Bureau/MASTER-COPY/master-basic.txt", "w")
        resolutionmastertxt.write("""[General]
Name=Sans nom

[Video]
BaseCX=1920
BaseCY=1080
OutputCX=1920
OutputCY=1080
ScaleType=lanczos
FPSType=0
FPSCommon=60

[Panels]
CookieId=2250AF64FAA0208F

[Output]
Mode=Simple

[SimpleOutput]
VBitrate=5500

[AdvOut]
TrackIndex=1
RecType=Standard
RecTracks=1
FLVTrack=1
FFOutputToFile=true
FFFormat=
FFFormatMimeType=
FFVEncoderId=0
FFVEncoder=
FFAEncoderId=0
FFAEncoder=
FFAudioMixes=1

[WebsocketAPI]
ServerEnabled=false
ServerPort=4444
LockToIPv4=false
DebugEnabled=false
AlertsEnabled=true
AuthRequired=false
AuthSecret=KNWnlEjudME3icDdtuPML4KIC34AFVg574lAhMI5sgc=
AuthSalt=QgBrvFzzjy3k7fj9D+osqDlAk/PkzT8v3BB4jShmgao=
         """)
        resolutionmastertxt.close()  
        time.sleep(1) 
        print("Changement de la résolution en cours...")
        srcresolution = r'/home/analogway/Bureau/MASTER-COPY/master-basic.txt'
        destresolution = r'/home/analogway/.config/obs-studio/basic/profiles/Sans nom/basic.ini' 
        shutil.copyfile(srcresolution, destresolution)
        print("Changement de la résolution terminé !")  

    if typeresolutionask is 3:
        print("Changement de la résolution pour de la 4K 30 FPS")
        resolutionmastertxt = open("/home/analogway/Bureau/MASTER-COPY/master-basic.txt", "w")
        resolutionmastertxt.write("""[General]
Name=Sans nom

[Video]
BaseCX=1920
BaseCY=1080
OutputCX=3840
OutputCY=2160
ScaleType=lanczos
FPSType=0
FPSCommon=30

[Panels]
CookieId=2250AF64FAA0208F

[Output]
Mode=Simple

[SimpleOutput]
VBitrate=5500

[AdvOut]
TrackIndex=1
RecType=Standard
RecTracks=1
FLVTrack=1
FFOutputToFile=true
FFFormat=
FFFormatMimeType=
FFVEncoderId=0
FFVEncoder=
FFAEncoderId=0
FFAEncoder=
FFAudioMixes=1

[WebsocketAPI]
ServerEnabled=false
ServerPort=4444
LockToIPv4=false
DebugEnabled=false
AlertsEnabled=true
AuthRequired=false
AuthSecret=KNWnlEjudME3icDdtuPML4KIC34AFVg574lAhMI5sgc=
AuthSalt=QgBrvFzzjy3k7fj9D+osqDlAk/PkzT8v3BB4jShmgao=
         """)
        resolutionmastertxt.close() 
        time.sleep(1)  
        print("Changement de la résolution en cours...")
        srcresolution = r'/home/analogway/Bureau/MASTER-COPY/master-basic.txt'
        destresolution = r'/home/analogway/.config/obs-studio/basic/profiles/Sans nom/basic.ini' 
        shutil.copyfile(srcresolution, destresolution)
        print("Changement de la résolution terminé !") 

    if typeresolutionask is 4:
        print("Changement de la résolution pour de la 4K 60 FPS")
        resolutionmastertxt = open("/home/analogway/Bureau/MASTER-COPY/master-basic.txt", "w")
        resolutionmastertxt.write("""[General]
Name=Sans nom

[Video]
BaseCX=1920
BaseCY=1080
OutputCX=3840
OutputCY=2160
ScaleType=lanczos
FPSType=0
FPSCommon=60

[Panels]
CookieId=2250AF64FAA0208F

[Output]
Mode=Simple

[SimpleOutput]
VBitrate=5500

[AdvOut]
TrackIndex=1
RecType=Standard
RecTracks=1
FLVTrack=1
FFOutputToFile=true
FFFormat=
FFFormatMimeType=
FFVEncoderId=0
FFVEncoder=
FFAEncoderId=0
FFAEncoder=
FFAudioMixes=1

[WebsocketAPI]
ServerEnabled=false
ServerPort=4444
LockToIPv4=false
DebugEnabled=false
AlertsEnabled=true
AuthRequired=false
AuthSecret=KNWnlEjudME3icDdtuPML4KIC34AFVg574lAhMI5sgc=
AuthSalt=QgBrvFzzjy3k7fj9D+osqDlAk/PkzT8v3BB4jShmgao=
         """)
        resolutionmastertxt.close()  
        time.sleep(1) 
        print("Changement de la résolution en cours...")
        srcresolution = r'/home/analogway/Bureau/MASTER-COPY/master-basic.txt'
        destresolution = r'/home/analogway/.config/obs-studio/basic/profiles/Sans nom/basic.ini' 
        shutil.copyfile(srcresolution, destresolution)
        print("Changement de la résolution terminé !")         


    typefluxask = int(input("Quelle type de flux vidéo souhaitez vous ? \n\n 1 - ndi \n 2 - rtsp \n 3 - rtmp (Seulement 1 flux vidéo) \n\n >> "))

    if typefluxask is 1:
        typefluxequal = "ndi"
        print("STARTING FLUX NDI = ", nbrflux)
        for fluxinput in range(nbrflux):
            ndimastertxt = open("/home/analogway/Bureau/MASTER-COPY/master-global.txt", "w")
            ndimastertxt.write("""[General]
Pre19Defaults=false
Pre21Defaults=false
Pre23Defaults=false
Pre24.1Defaults=false
FirstRun=true
LastVersion=453115908

[Basic]
Profile=Sans nom
ProfileDir=Sans nom
SceneCollection=Sans nom
SceneCollectionFile=Sans nom

[BasicWindow]
gridMode=false
geometry=AdnQywADAAD////9////9gAAB1cAAAhKAAAAAAAAABQAAAdUAAAIRwAAAAAAAAAADwAAAAAAAAAAFAAAB1QAAAhH
DockState=AAAA/wAAAAD9AAAAAQAAAAMAAAdVAAABw/wBAAAABvsAAAAUAHMAYwBlAG4AZQBzAEQAbwBjAGsBAAAAAAAAAR0AAACgAP////sAAAAWAHMAbwB1AHIAYwBlAHMARABvAGMAawEAAAEjAAABGgAAAKAA////+wAAABIAbQBpAHgAZQByAEQAbwBjAGsBAAACQwAAAj8AAADcAP////sAAAAeAHQAcgBhAG4AcwBpAHQAaQBvAG4AcwBEAG8AYwBrAQAABIgAAAEOAAAAmgD////7AAAAGABjAG8AbgB0AHIAbwBsAHMARABvAGMAawEAAAWcAAABuQAAAPMA////+wAAABIAcwB0AGEAdABzAEQAbwBjAGsCAAAGIgAAA9QAAAK8AAAAyAAAB1UAAAY8AAAABAAAAAQAAAAIAAAACPwAAAAA
ExtraBrowserDocks=[]
PreviewEnabled=true
AlwaysOnTop=false
SceneDuplicationMode=true
SwapScenesMode=true
EditPropertiesMode=false
PreviewProgramMode=false
DocksLocked=false
ShowStatusBar=true

[scripts-tool]
prevScriptRow=-1

[ScriptLogWindow]
geometry=AdnQywADAAAAAAAAAAAAFAAAAlcAAAGjAAAAAAAAABQAAAJXAAABowAAAAAAAAAADwAAAAAAAAAAFAAAAlcAAAGj

[NDIPlugin]
MainOutputEnabled=true
MainOutputName=OUTPUT="""+str(fluxinput)+"""
PreviewOutputEnabled=true
PreviewOutputName=test

[PropertiesWindow]
cx=720
cy=580

[WebsocketAPI]
AuthSetupPrompted=true
""")
            ndimastertxt.close()
            print("Préparation terminé de l'input ", nbrflux)
            srcndi = r'/home/analogway/Bureau/MASTER-COPY/master-global.txt'
            destndi = r'/home/analogway/.config/obs-studio/global.ini'
            shutil.copyfile(srcndi, destndi)
            print("Transfert Terminé du global.ini pour l'input", nbrflux)
            print("Lancement d'OBS pour l'input ", nbrflux)
            os.popen('obs -m')
            time.sleep(1)
    elif typefluxask is 2:
        typefluxequal = "rtsp"
        print("STARTING FLUX RTSP = ", nbrflux)
        for fluxinput in range(nbrflux):
            rtspmastertxt = open("/home/analogway/Bureau/MASTER-COPY/master-rtsp_output.txt", "w")
            rtspmastertxt.write("""{"authentication":false,"port":159"""+str(fluxinput)+"""}""")
            rtspmastertxt.close()
            print("Préparation terminé de l'input ", nbrflux)
            srcrtsp = r'/home/analogway/Bureau/MASTER-COPY/master-rtsp_output.txt'
            destrtsp = r'/home/analogway/.config/obs-studio/plugin_config/obs-rtspserver/rtsp_output.json'
            shutil.copyfile(srcrtsp, destrtsp)
            print("Transfert Terminé du rtsp_output.json pour l'input", nbrflux)
            print("Lancement d'OBS pour l'input ", nbrflux)
            os.popen('obs -m')
            time.sleep(1)
            pyautogui.hotkey('ctrl', 'shift', 'à')
            time.sleep(2)

    elif typefluxask is 3:
        typefluxequal = "rtmp"
        print("STARTING FLUX RTMP = ", nbrflux)
        for fluxinput in range(nbrflux):
            rtmpmastertxt = open("/home/analogway/Bureau/MASTER-COPY/master-service.txt", "w") 
            rtmpmastertxt.write("""{"settings":{"bwtest":false,"key":"","server":"rtmp://192.168.3.1:193"""+str(fluxinput)+"""/live","use_auth":false},"type":"rtmp_custom"}""")    
            rtmpmastertxt.close()
            print("Préparation terminé de l'input ", nbrflux)
            srcrtmp = r'/home/analogway/Bureau/MASTER-COPY/master-service.txt'
            destrtmp = r'/home/analogway/.config/obs-studio/basic/profiles/Sans nom/service.json'
            shutil.copyfile(srcrtmp, destrtmp)
            print("Transfert Terminé du service.json pour l'input", nbrflux)
            print("Lancement d'OBS pour l'input ", nbrflux)
            os.popen('obs -m --startstreaming')
            time.sleep(1)
            


        


        

        

        













#Script Start


main()
