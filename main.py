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

    # Turn 90 degrees, value will be different for you, im on a 4k monitor
    flipMouseMove = 1000

    # Making tuple with data from the window for later use
    region = (newWorldWindow.left, newWorldWindow.top, newWorldWindow.width, newWorldWindow.height)

    # Savoir si l'on est dans le jeu, ou dans le fenêtre de démarrage.
    ingame = False

    # Main bot loop, runs forever use CTRL+C to turn it off
    while True:
        if ingame is False:
            print("On est pas en jeu. On cherche à ce connecter.")
            pyautogui.press('j')
            time.sleep(.5)
            if pyautogui.locateOnScreen("imgs/ingame.png", grayscale=True, confidence=.65, region=region) is not None:
                print("On est déjà en jeu.")
                pyautogui.press('j')
                ingame = True
                continue
            if pyautogui.locateOnScreen("imgs/continue.png", grayscale=True, confidence=.50, region=region) is not None:
                posContinue = pyautogui.locateOnScreen("imgs/continue.png")
                if posContinue is not None:
                    print("On a trouvé le premier Ecran de lancement.")
                    pyautogui.moveTo(posContinue[0] + (posContinue[2]/3), posContinue[1] + (posContinue[3]/3))
                    clicage()
                else:
                    print("Bug 1")
            if pyautogui.locateOnScreen("imgs/continue0.png", grayscale=True, confidence=.50, region=region) is not None:
                posContinue1 = pyautogui.locateOnScreen("imgs/continue0.png")
                if posContinue1 is not None:
                    print("On a trouvé le premier Ecran de lancement.")
                    pyautogui.moveTo(posContinue1[0] + (posContinue1[2]/3), posContinue1[1] + (posContinue1[3]/3))
                    clicage()
                else:
                    print("Bug 2")
            if pyautogui.locateOnScreen("imgs/jouer.png", grayscale=True, confidence=.50, region=region) is not None:
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
            # Find that image on screen, in that region, with a confidence of 65%
            print("On est en jeu, on peut farmer.")
            if pyautogui.locateOnScreen("imgs/e0.png", grayscale=True, confidence=.65, region=region) is not None and peche is False:
                print("On récolte")
                pyautogui.press('e')
                if pyautogui.locateOnScreen("imgs/pioche5.png", grayscale=True, confidence=.90, region=region) is not None:
                    print("On récole du pierre.")
                    while pyautogui.locateOnScreen("imgs/pioche5.png", grayscale=True, confidence=.90, region=region) is not None:
                        time.sleep(.1)
                elif pyautogui.locateOnScreen("imgs/hache5.png", grayscale=True, confidence=.90, region=region) is not None:
                    print("On récolte de la bois.")
                    while pyautogui.locateOnScreen("imgs/hache5.png", grayscale=True, confidence=.90, region=region) is not None:
                        time.sleep(.1)
                print("On a fini de récolter")
                continue

            peche = False
            if pyautogui.locateOnScreen("imgs/peche4.png", grayscale=True, confidence=.85, region=region) is not None:
                print("On passe en mode je pêche.")
                while pyautogui.locateOnScreen("imgs/peche4.png", grayscale=True, confidence=.85, region=region) is not None:
                    #on reste en mode peche
                    print("Et go pêcher.")
                    if pyautogui.locateOnScreen("imgs/lancer.png", grayscale=True, confidence=.60, region=region) is not None or pyautogui.locateOnScreen("imgs/attentepeche.png", grayscale=True, confidence=.85, region=region) is not None:
                        if pyautogui.locateOnScreen("imgs/attentepeche.png", grayscale=True, confidence=.60, region=region) is None:
                            pyautogui.mouseDown()
                            time.sleep(2 * random.random())
                            pyautogui.mouseUp()
                            time.sleep(2)
                        print("On attend que ca morde")
                        while pyautogui.locateOnScreen("imgs/attentepeche.png", grayscale=True, confidence=.60, region=region) is not None:
                            time.sleep(.1)
                        print("Ca mord !!!")
                        pyautogui.click()
                        while pyautogui.locateOnScreen("imgs/lancer.png", grayscale=True, confidence=.60, region=region) is None:
                            print("On remonte le poisson")
                            pyautogui.mouseDown()
                            time.sleep(.3 * random.random())
                            pyautogui.mouseUp()
                            time.sleep(.2 * random.random())
                        print("Parfait, maintenant ANTIAFK!")
                        # Pour l'animation si gros poissons
                        time.sleep(5)
                        pyautogui.keyDown('d')
                        time.sleep(.5)
                        pyautogui.keyUp('d')
                        pyautogui.keyDown('a')
                        time.sleep(.5)
                        pyautogui.keyUp('a')
                        print("Fini ce tour. On reprend")
                        continue
            else:
                # Do I got to explain?
                pyautogui.keyDown('w')

                # Randomly move foward 0 - 1.5 seconds
                temp = 1.5 * random.random()
                currentFoward += temp
                time.sleep(temp)

                # Brah, you know
                pyautogui.keyUp('w')

                # Flippy flip if you hitty hit the max move time (fowardMoveTotal)
                if currentFoward >= fowardMoveTotal:
                    # Reset the move foward
                    currentFoward = 0

                    # Move the mouse 90 degrees
                    pydirectinput.move(flipMouseMove * flip, 1, relative=True)

                    # Move Foward 1.5 secs
                    pyautogui.keyDown('w')
                    time.sleep(1.5)
                    pyautogui.keyUp('w')

                    # Move the mouse 90 degrees
                    pydirectinput.move(flipMouseMove * flip, 1, relative=True)

                    # Flippy flippy the value. Evil math.
                    flip *= -1

                # Sleeping for the animation
                time.sleep(.1)


# Runs the main function
if __name__ == '__main__':
    print("On démarre le Bot")
    main()