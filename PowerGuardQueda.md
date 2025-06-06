PowerGuardQueda.py
Descrição
O PowerGuardQueda.py é um sistema de detecção automática de quedas utilizando visão computacional e inteligência artificial. Ele utiliza a biblioteca MediaPipe para identificar a pose corporal de uma pessoa usando a webcam e, caso detecte uma possível queda, emite um alarme sonoro.

Como funciona
Captura de Vídeo: O sistema utiliza a webcam do computador para capturar imagens em tempo real.
Detecção de Pose: Com a biblioteca MediaPipe, o código identifica pontos-chave do corpo humano, especialmente ombros e quadris.
Lógica de Queda: O sistema calcula a diferença vertical entre os ombros e os quadris. Se esses pontos estiverem muito próximos na vertical (indicando que a pessoa está deitada, possivelmente após uma queda), aciona um alerta.
Alarme Sonoro: Se uma queda for detectada, um alarme sonoro é tocado repetidamente até que a situação volte ao normal.

Interface Visual: O status é exibido na janela do vídeo:
"Status: OK" em verde quando tudo está normal.
"🚨 QUEDA DETECTADA 🚨" em vermelho quando é identificada uma possível queda.

Requisitos
Python 3.x
OpenCV (cv2)
MediaPipe
Pygame
Para instalar as dependências, execute:

bash
pip install opencv-python mediapipe pygame
Como usar
Certifique-se de que você tem uma webcam conectada ao seu computador.
Coloque um arquivo de áudio de alarme chamado alarm-26718.mp3 na mesma pasta do script (ou altere a linha 10 para o nome correto do seu arquivo de áudio).
Execute o script:
bash
python PowerGuardQueda.py
A janela do vídeo será aberta e o sistema começará a monitorar automaticamente.
Funcionamento do Alarme
O alarme sonoro só toca quando uma queda é detectada.
Assim que a pessoa retorna à posição normal (em pé), o alarme para automaticamente.
Observações
O sistema utiliza a tecla ESC para encerrar a aplicação.
A detecção de quedas é baseada na distância vertical entre ombros e quadris — pode haver falsos positivos caso a pessoa se sente ou deite propositalmente.
Para maior robustez, recomenda-se ajustar a sensibilidade conforme o uso real.
