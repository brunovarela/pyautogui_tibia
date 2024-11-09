Projeto de Automação de Clicke no Tibia
Esse é um projeto em Python que automatiza o clique em itens e no personagem no jogo Tibia. Através de teclas de atalho configuradas (F1 e F2), o script realiza ações de uso de itens específicos, como mana potion e ultimate healing (UH), simulando o movimento e clique do mouse em pontos pré-definidos na tela. Isso ajuda a automatizar a utilização de poções para manter o personagem curado ou regenerar mana.

Funcionalidades
Definição de posições: O usuário pode definir as posições da mana potion, UH e do personagem na tela.
Automação de cliques: Ao pressionar F1, o script clica automaticamente no local da mana potion e depois no personagem, simulando o uso da mana potion. O mesmo acontece com F2 para o UH.
Controle de uso único por pressionamento: Cada tecla acionada realiza uma única ação até que a tecla seja liberada e pressionada novamente, evitando múltiplos cliques desnecessários.
Pré-requisitos
Python 3.x
Bibliotecas:
keyboard: para detectar os pressionamentos das teclas.
pyautogui: para capturar a posição do mouse e realizar movimentos e cliques automáticos.
time: para pausas e intervalos entre cliques.
Para instalar as bibliotecas, use:

bash
Copiar código
pip install keyboard pyautogui
Nota: Este script deve ser executado em modo de administrador para que a biblioteca keyboard funcione corretamente.

Configuração e Uso
Defina as posições na tela:

Execute o script e siga as instruções.
Posicione o mouse sobre a mana potion, pressione Ctrl+A.
Posicione o mouse sobre o UH e pressione Ctrl+A novamente.
Por fim, posicione o mouse sobre o personagem e pressione Ctrl+A.
Ações com teclas de atalho:

Pressione F1 para usar a mana potion.
Pressione F2 para usar o UH.
Execução contínua:

O script continua ativo e reseta as variáveis de controle para que você possa repetir as ações ao pressionar as teclas novamente.
Atenção: Use com responsabilidade e siga as políticas de uso do Tibia, evitando qualquer risco de violar os Termos de Serviço do jogo.

Licença
Este projeto é de uso pessoal e educativo e não possui licença específica.
