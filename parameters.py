'''
    parameter N: number of files present in the origin servers on the internet.
    Assume this to be fairly large, say 1000+
'''
N=1000

'''
    Pareto Distribution Parameters:
        1) alpha = shape parameter of the pareto distribution. (> 1)
        2) k = lower bound on the pareto distribution. ( achieve mean ~ 1)
'''
alpha_s = 4
k_s = 0.8
alpha_p = 3
k_p = 0.3

'''
    Poisson Distribution Parameters:

'''
poisson_lambda= 100
number_of_requests = 1000

'''
    Simulation parameters
'''
iterations = 200
cache_capacity = 50
network_transmission_rate = 20
cache_transmission_rate = 200
