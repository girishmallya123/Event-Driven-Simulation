import numpy as np
import logging
from exceptions import InvalidParameterException

def verify_pareto_params(x_m, alpha, mu):
    #TODO: Implement the param check
    return True

def generate_pareto_samples(params):
    x_m, alpha = params.k, params.alpha
    mu = calculate_pareto_mean(alpha, x_m)
    if not verify_pareto_params:
        raise InvalidParameterException

    logging.info("pareto_sampler# Generating a pareto distribution mean {}".format(mu))
    

    #drawing samples from distribution
    samples = (np.random.pareto(alpha, 1000) + 1) * x_m
    return samples

def calculate_pareto_mean(alpha, x_m):
    return float(float(alpha*x_m)/float(alpha-1))
