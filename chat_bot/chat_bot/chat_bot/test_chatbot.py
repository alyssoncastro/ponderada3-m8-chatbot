#! /bin/env python3

import rclpy
from rclpy.node import Node
import re



class RoboChatbot(Node):
    def __init__(self):
        super().__init__('robo_chatbot_node')
        self.get_logger().info("RoboChatbot Node Iniciado")
        self.intent_patterns = {
            r"\b[Vv]á\spara\s([a-zA-Z\s]+)": "mover_para_destino",
            r"\b[Mm]e\sleve\saté\s([a-zA-Z\s]+)": "mover_para_destino"
        }

        # Ação para mover o robô
        self.acoes = {
            "mover_para_destino": lambda destino: f"OK! Seu comando recebido, movendo para {destino}."
        }
        self.processar_comandos()



    def processar_comandos(self):
        # Loop para processar comandos de entrada
        while True:
            comando = input("Como posso ajudar hoje? (digite 'sair' para encerrar, tá ok?): ")
            if comando.lower() == 'sair':
                break

            for expressao, intencao in self.intent_patterns.items():
                resultado = re.search(expressao, comando)
                # executando a ação correspondente e informa
                if resultado:
                    self.get_logger().info(self.acoes[intencao](resultado.group(1)))
                    break
            else:
                # Se nenhum comando for reconhecido.
                self.get_logger().info("Me desculpa, mas não consegui entender.")


def main(args=None):
    rclpy.init(args=args)
    node = RoboChatbot()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
