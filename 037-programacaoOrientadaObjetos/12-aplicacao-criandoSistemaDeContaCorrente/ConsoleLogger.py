import sys
import logging

class ConsoleLogger:
    def __init__(self, log_file):
        self.log_file = log_file
        self.log = logging.getLogger('console_logger')
        self.log.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(message)s')

        # Redireciona as mensagens para o arquivo de log
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)
        self.log.addHandler(file_handler)

        # Redireciona as mensagens para o console
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(formatter)
        self.log.addHandler(console_handler)

        # Redireciona sys.stdout para o logger personalizado
        sys.stdout = self

    def write(self, message):
        self.log.info(message)

    def flush(self):
        pass


