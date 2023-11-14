# ChatBot Com ROS2 

### Autor: Alysson C. C. Cordeiro 
#### Módulo 8 - Engenharia da Computação - INTELI 
--- 
## Descrição:

Projeto com um chatbot simpples e com ROS2, programado para interagir com robô TurtleBot 3.

## Quais tecnologias prinicipais?

1. ROS2;
2. Linguagem Python;

## Como ele funciona?

O chatbot obedece quando você diz algumas ações como, por exemplo, "Vá para...", "Me leve até..." ou "Dirija-se". Além de contar com um dicinários de ações. Além disso, ele também te dar um feedback.

## Como faço para instalar?

obs: verifique se o ROS2 e python estejam instalado na sua máquina.

1. Clone o repositório:

```bash
   cd seu_workspace
   git clone https://github.com/alyssoncastro/ponderada3-m8-chatbot.git
   cd chat_bot
```
2. Agora dê um Colcon:

```bash
colcon build
```

3. Fonte o ambiente ROS2:

```bash
source install/setup.zsh
```

4. Executando:

```bash
ros2 run chat_bot test_chatbot
```

## Veja o vídeo no link abaixo:

https://drive.google.com/file/d/1--Vf-gpBZmy5opIxhDe7NQDbh5tlD6el/view?usp=sharing


NOTA: para o professor Nicola. Sempre é bom feedback. E agradecê-lo pela compreensão do meu esforço. Mesmo o projeto e chatbot não saindo perfeito.

