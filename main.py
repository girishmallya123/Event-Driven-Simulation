import logging
from config_reader import Config


def main():
    logging.basicConfig(filename='event.log', level=logging.INFO)
    logging.info("main#Starting the simulator")
    params = Config()

if __name__ == "__main__":
    main()
