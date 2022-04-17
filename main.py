import logging
from config_reader import Config
import pareto_sampler
from exceptions import InvalidParameterException
import sys

def main():
    logging.basicConfig(filename='event.log', level=logging.INFO)
    logging.info("main#Starting the simulator")
    params = Config()
    try:
        file_sizes = pareto_sampler.generate_pareto_samples(params)
    except InvalidParameterException:
        logging.error("main# Exitting because the parameters are invalid to generate a pareto distribution of file sizes")
        sys.exit(0)
    print(file_sizes)
if __name__ == "__main__":
    main()
