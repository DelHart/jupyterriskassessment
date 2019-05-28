import numpy as np

# we use 3 parameters, but some of the distributions only need 2
# todo: add more checking / modification to make sure the parameters make sense for the distribution
def chisquare_fn(a, b, size):
    return np.random.chisquare (a, size)

def exp_fn(a, b, size):
    return np.random.exponential (a, size)

def geo_fn(a, b, size):
    return np.random.geometric (a, size)

def poisson_fn(a, b, size):
    return np.random.poisson (a, size)

def weibull_fn(a, b, size):
    return np.random.weibull (a, size)

# this one has more details than qual
update_triage_stmt = '''UPDATE detailv SET name = %s, description = %s, vulnerability = %s, vdist = %s, vparam2 = %s,
                                           pervasive = %s, pdist = %s, pparam2 = %s,
                                           impact = %s, impact_name = %s, impact_description = %s, impact_dist = %s, impact_param2 = %s,
                                           source_name = %s, source_description = %s, capacity = %s, cap_dist = %s, cap_param2 = %s,
                                           init = %s, init_dist = %s, init_param2 = %s
                        WHERE threat_id = %s AND source_id = %s AND impact_id = %s'''


# a mapping of distributions
prob_dict = { 'normal' : 0, 'beta' : 1, 'binomial': 2, 'chisquare' : 3, 'exponential': 4, 'gamma' : 5, 'geometric': 6, 'poisson' : 7, 'uniform' : 8, 'weibull' : 9}
prob_rdict = {}
for x in prob_dict.keys():
    prob_rdict[prob_dict[x]] = x
    
prob_list = prob_dict.keys()

prob_fn = { 'normal' : np.random.normal, 'beta' : np.random.beta,
            'binomial': np.random.binomial, 'chisquare' : chisquare_fn,
            'exponential': exp_fn, 'gamma' : np.random.gamma, 'geometric': geo_fn,
            'poisson' : poisson_fn, 'uniform' : np.random.uniform, 'weibull' :
            weibull_fn}


