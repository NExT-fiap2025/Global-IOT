# Global-IOT

PowerGuardGesto
Este projeto implementa um sistema de detecção de gestos utilizando visão computacional para acionar um alarme sonoro em situações de emergência. Ele foi desenvolvido em Python, utilizando as bibliotecas OpenCV, MediaPipe e pygame.

Objetivo
O sistema monitora a imagem da webcam e detecta quando duas mãos estão visíveis no quadro. Ao identificar esse gesto (duas mãos levantadas), assume-se uma situação de emergência, tocando um alarme sonoro e exibindo um aviso na tela.

Como funciona
Captura de vídeo: Utiliza a webcam do computador para capturar imagens em tempo real.
Detecção de mãos: Utiliza a biblioteca MediaPipe para detectar e rastrear as mãos presentes no vídeo.
Reconhecimento de gesto: Se duas mãos forem detectadas ao mesmo tempo, considera-se um gesto de pedido de ajuda.
Alarme sonoro: Um alarme (arquivo alarm-26718.mp3) é reproduzido enquanto o gesto permanece.
Interface: A janela exibe o número de mãos detectadas ou o alerta de emergência, conforme o caso.
Instalação
Antes de rodar o código, instale as dependências necessárias:

bash
pip install opencv-python mediapipe pygame
Coloque o arquivo de áudio alarm-26718.mp3 na mesma pasta do script.

Como usar
Execute o script Python:

bash
python PowerGuardGesto.py
A webcam será ativada e a janela do sistema será aberta. Ao levantar as duas mãos para a câmera, o alarme tocará e será exibida a mensagem de emergência na tela. Para encerrar o programa, pressione a tecla ESC.

Estrutura do Código
tocar_alarme(): Função responsável por iniciar o alarme sonoro.
parar_alarme(): Função responsável por parar o alarme.
Loop principal: Captura quadros da webcam, processa-os para detectar mãos e aciona/desativa o alarme conforme o gesto identificado.
Requisitos
Python 3.x
Webcam funcional
Bibliotecas: opencv-python, mediapipe, pygame
Observações
O sistema detecta apenas o gesto de mostrar duas mãos simultaneamente.
O arquivo de áudio do alarme deve estar presente na pasta do script.
