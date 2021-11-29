from PIL.ImageOps import grayscale
from cv2 import grabCut
from pynput import keyboard
import pyautogui
import pydirectinput
import time
import random
import queue

def clicage():
    randomwait = 1.1 * random.random()
    time.sleep(randomwait)
    pyautogui.click()
    time.sleep(randomwait)

def main():
    """
    Main function for the program
    """

    # Finds all Windows with the title "New World"
    newWorldWindows = pyautogui.getWindowsWithTitle("New World")

    # Find the Window titled exactly "New World" (typically the actual game)
    for window in newWorldWindows:
        if window.title == "New World":
            newWorldWindow = window
            break

    # Select that Window
    newWorldWindow.activate()

    # Move your mouse to the center of the game window
    centerW = newWorldWindow.left + (newWorldWindow.width/3*2)
    centerH = newWorldWindow.top + (newWorldWindow.height/3*2)
    pyautogui.moveTo(centerW, centerH)

    # Clicky Clicky
    clicage()

    # Seconds to move foward
    fowardMoveTotal = 20

    # Current seconds foward moved
    currentFoward = 0

    # Go right or left
    flip = 1

    # Turn 90 degrees, value will be different for you
    flipMouseMove = 1000

    # Making tuple with data from the window for later use
    region = (newWorldWindow.left, newWorldWindow.top, newWorldWindow.width, newWorldWindow.height)

    # Savoir si l'on est dans le jeu, ou dans le fenêtre de démarrage.
    ingame = False

    # Main bot loop, runs forever use CTRL+C to turn it off
    while True:
        # Chargement du jeu
        if pyautogui.locateOnScreen("imgs/tropplein.png", grayscale=False, confidence=.65, region=region) is not None:
            # On est trop chargé, on arrête tout le farm
            print("Trop plein ... on attent que tu te vide tout seul ou que tu prennes une potion.")
            time.sleep(10)
        else:
            # On peut farmer, on est pas plein.
            if ingame is False:
                print("On est pas en jeu. On cherche à ce connecter.")
                pyautogui.press('j')
                time.sleep(.5)
                if pyautogui.locateOnScreen("imgs/ingame.png", grayscale=True, confidence=.65, region=region) is not None:
                    print("On est déjà en jeu.")
                    pyautogui.press('j')
                    ingame = True
                    continue
                if pyautogui.locateOnScreen("imgs/continue.png", grayscale=True, confidence=.5, region=region) is not None:
                    posContinue = pyautogui.locateOnScreen("imgs/continue.png")
                    if posContinue is not None:
                        print("On a trouvé le premier Ecran de lancement.")
                        pyautogui.moveTo(posContinue[0] + (posContinue[2]/3), posContinue[1] + (posContinue[3]/3))
                        clicage()
                    else:
                        print("Bug 1")
                if pyautogui.locateOnScreen("imgs/continue0.png", grayscale=True, confidence=.5, region=region) is not None:
                    posContinue1 = pyautogui.locateOnScreen("imgs/continue0.png")
                    if posContinue1 is not None:
                        print("On a trouvé le premier Ecran de lancement.")
                        pyautogui.moveTo(posContinue1[0] + (posContinue1[2]/3), posContinue1[1] + (posContinue1[3]/3))
                        clicage()
                    else:
                        print("Bug 2")
                if pyautogui.locateOnScreen("imgs/jouer.png", grayscale=True, confidence=.5, region=region) is not None:
                    time.sleep(.5)
                    posJouer = pyautogui.locateOnScreen("imgs/jouer.png")
                    if posJouer is not None:
                        print("On a trouvé le premier Ecran des personnages.")
                        pyautogui.moveTo(posJouer[0] + (posJouer[2]/3), posJouer[1] + (posJouer[3]/3))
                        clicage()
                        ingame = True
                        continue
                    else:
                        print("Bug 3")
            else:
                if pyautogui.locateOnScreen("imgs/peche4.png", grayscale=True, confidence=.85, region=region) is not None:
                    # On passe en mode Pêche
                    print("On passe en mode je pêche.")
                    while pyautogui.locateOnScreen("imgs/peche4.png", grayscale=True, confidence=.85, region=region) is not None:
                        # On reste en mode peche
                        if pyautogui.locateOnScreen('imgs/pause.png', grayscale=True, confidence=.65, region=region) is not None:
                            #On met le bot en pause
                            print("Bot en pause")
                            time.sleep(5)
                        else:
                            print("Et go pêcher.")
                            if pyautogui.locateOnScreen("imgs/lancer.png", grayscale=True, confidence=.65, region=region) is not None or pyautogui.locateOnScreen("imgs/attentepeche.png", grayscale=True, confidence=.85, region=region) is not None:
                                if pyautogui.locateOnScreen("imgs/attentepeche.png", grayscale=True, confidence=.65, region=region) is None:
                                    pyautogui.mouseDown()
                                    time.sleep(2 * random.random() + 0.5)
                                    pyautogui.mouseUp()
                                    time.sleep(2)
                                print("On attend que ca morde")
                                while pyautogui.locateOnScreen("imgs/attentepeche.png", grayscale=True, confidence=.65, region=region) is not None:
                                    time.sleep(.05)
                                print("Ca mord !!!")
                                pyautogui.click()
                                while pyautogui.locateOnScreen("imgs/lancer.png", grayscale=True, confidence=.85, region=region) is None:
                                    print("On remonte le poisson")
                                    pyautogui.mouseDown()
                                    while pyautogui.locateOnScreen('imgs/nodanger.png', grayscale=True, confidence=.65) is not None:
                                        time.sleep(.1)
                                    pyautogui.mouseUp()
                                    time.sleep(.3 * random.random())
                                pyautogui.press('escape')
                                time.sleep(3)
                                pyautogui.press('escape')
                                # Pour l'animation si gros poissons
                                if pyautogui.locateOnScreen('imgs/antiafk.png', grayscale=True, confidence=.65, region=region):
                                    print("Anti AFK détecté.")
                                    pyautogui.keyDown('d')
                                    time.sleep(.5)
                                    pyautogui.keyUp('d')
                                    time.sleep(.5)
                                    pyautogui.keyDown('a')
                                    time.sleep(.5)
                                    pyautogui.keyUp('a')
                                    time.sleep(2)
                                    pyautogui.press('tab')
                                    posReparer = pyautogui.locateOnScreen('imgs/reparer.png')
                                    pyautogui.moveTo(posReparer[0] + (posReparer[2]/2), posReparer[1] + (posReparer[3]/2))
                                    clicage()
                                    posReparer = pyautogui.locateOnScreen('imgs/reparer1.png')
                                    pyautogui.moveTo(posReparer[0] + (posReparer[2]/2), posReparer[1] + (posReparer[3]/2))
                                    clicage()
                                    pyautogui.press('tab')
                                else:
                                    time.sleep(1)
                                print("Fini ce tour. On reprend")
                                continue
                else:
                    if pyautogui.locateOnScreen('imgs/pause.png', grayscale=True, confidence=.65, region=region) is not None:
                        #On met le bot en pause
                        print("Bot en pause")
                        time.sleep(5)
                    else:
                        print("On est en jeu, on peut farmer.")

                        # Do I got to explain?
                        pyautogui.keyDown('w')

                        while pyautogui.locateOnScreen("imgs/e0.png", grayscale=True, confidence=.65, region=region) is None:
                            time.sleep(.05)
                            
                        pyautogui.keyUp('w')
                        
                        print("On récolte")
                        pyautogui.press('e')
                        if pyautogui.locateOnScreen("imgs/pioche5.png", grayscale=True, confidence=.9, region=region) is not None:
                            print("On récole de la pierre.")
                            while pyautogui.locateOnScreen("imgs/pioche5.png", grayscale=True, confidence=.9, region=region) is not None:
                                time.sleep(.01)
                        elif pyautogui.locateOnScreen("imgs/hache5.png", grayscale=True, confidence=.9, region=region) is not None:
                            print("On récolte du bois.")
                            while pyautogui.locateOnScreen("imgs/hache5.png", grayscale=True, confidence=.9, region=region) is not None:
                                time.sleep(.01)
                        elif pyautogui.locateOnScreen("imgs/recolter4.png", grayscale=True, confidence=.9, region=region) is not None:
                            print("On recolte des herbes.")
                            while pyautogui.locateOnScreen("imgs/recolter4.png", grayscale=True, confidence=.9, region=region) is not None:
                                time.sleep(.01)
                        else:
                            print("On récolte un truc sans outil")
                            while pyautogui.locateOnScreen("imgs/enrecolte.png", grayscale=True, confidence=0.65, region=region) is not None:
                                time.sleep(.01)
                        print("On a fini de récolter")
                        continue


# Runs the main function
if __name__ == '__main__':
    print("On démarre le Bot")
    main()