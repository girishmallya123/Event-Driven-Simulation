import parameters

class Config:
    def __init__(self):
        self.N = parameters.N
        self.k_s = parameters.k_s
        self.k_p = parameters.k_p
        self.alpha_s = parameters.alpha_s
        self.alpha_p = parameters.alpha_p
        self.poisson_lambda = parameters.poisson_lambda
        self.number_of_requests = parameters.number_of_requests
        self.iterations = parameters.iterations
        self.cache_capacity = parameters.cache_capacity
        self.network_transmission_rate = parameters.network_transmission_rate
        self.cache_transmission_rate = parameters.cache_transmission_rate
