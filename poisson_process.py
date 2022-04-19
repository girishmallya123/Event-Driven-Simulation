import logging
import random
import math

def poisson_process(lambda_val, number_of_arrivals):
    res = []
    arrival_time = 0
    logging.info("poisson_process# Generating a poisson distribution with lambda {}".format(lambda_val))
    for i in range(number_of_arrivals):
        p = random.random()
        _inter_arrival_time = -math.log(1.0-p)/lambda_val
        arrival_time = arrival_time + _inter_arrival_time
        res.append(arrival_time)
    return res
