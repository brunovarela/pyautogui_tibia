import keyboard
import pyautogui
import time

def get_user_mouse_positions():
    """
    Prompts the user to press Ctrl+A to input a mouse position, then returns it as a tuple.
    """
    # Wait for the user to press Ctrl+A
    keyboard.wait('ctrl+a')
    
    # Get the user's mouse position
    x, y = pyautogui.position()
    print(f"Position: ({x}, {y})")
    
    return x, y

def click_positions(heal, character):
    """
    Clica com o botão direito na posição da mana potion e com o botão esquerdo na posição do personagem.
    """
    pyautogui.moveTo(heal[0], heal[1])
    time.sleep(0.1)
    pyautogui.click(button="right")
    time.sleep(0.2)
    pyautogui.moveTo(character[0], character[1])
    time.sleep(0.1)
    pyautogui.click(button="left")  # Especifica que o clique é com o botão esquerdo
    

if __name__ == "__main__":
    print("Aperte Control+A em cima da mana potion")
    x_mana, y_mana = get_user_mouse_positions()

    print("Aperte Control+A em cima da UH")
    x_uh, y_uh = get_user_mouse_positions()

    print("Aperte Control+A em cima do seu personagem")
    x_char, y_char = get_user_mouse_positions()

    print("Pressione F1 para usar a mana potion")
    print("Pressione F2 para usar a UH")

    # Variáveis de controle para execução única
    f1_action_executed = False
    f2_action_executed = False

    def use_mana_potion():
        global f1_action_executed
        if not f1_action_executed:
            click_positions((x_mana, y_mana), (x_char, y_char))
            f1_action_executed = True
            print("Mana potion usada.")

    def use_uh():
        global f2_action_executed
        if not f2_action_executed:
            click_positions((x_uh, y_uh), (x_char, y_char))
            f2_action_executed = True
            print("UH usada.")

    # Registra os eventos de pressionamento das teclas F1 e F2
    keyboard.on_press_key('f1', lambda _: use_mana_potion())
    keyboard.on_press_key('f2', lambda _: use_uh())

    # Loop principal para resetar as variáveis quando as teclas são liberadas
    while True:
        # Redefine as variáveis quando as teclas são liberadas
        if not keyboard.is_pressed('f1'):
            f1_action_executed = False
        if not keyboard.is_pressed('f2'):
            f2_action_executed = False

        # Pequena pausa para evitar o uso excessivo da CPU
        time.sleep(0.1)
