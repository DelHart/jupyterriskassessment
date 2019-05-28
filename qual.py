
# data entered through other notebooks might be outside the range 0 - 100
# check for that and return the best value that is appropriate for this notebook

def norm (x):
    if (x > 100):
        return 100
    if (x < 1):
        return 1
    return x


new_triage_stmt = '''INSERT INTO triagev (name, description, vulnerability, pervasive, impact, impact_name, impact_description, source_name, source_description, capacity, init)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''

update_triage_stmt = '''UPDATE triagev SET name = %s, description = %s, vulnerability = %s, pervasive = %s, 
                                           impact = %s, impact_name = %s, impact_description = %s, 
                                           source_name = %s, source_description = %s, capacity = %s, init = %s
                        WHERE threat_id = %s AND source_id = %s AND impact_id = %s'''



# derived from NIST SP800-30
qscale = ['very low', 'low', 'moderate', 'high', 'very high']
qrange = [5, 20, 70, 95, 101]
qdict = {}
qval_dict = {'very low' : 3, 'low' : 13, 'moderate' : 50, 'high' : 87, 'very high' : 97}
lower = 0
for x in range(0, len(qrange)):
    for y in range(lower, qrange[x]):
        qdict[y]=qscale[x]
    lower = qrange[x]


# multiply the rate by the likelihood to get the number per year
rate_dict = {'very low' : .0003 , 'low' : .01, 'moderate' : .1, 'high' : .85, 'very high' : 4}

# multiply the loss factor by the impact to get a loss per event, result is percent of company annual revenue
loss_dict = {'very low' : .004 , 'low' : .008, 'moderate' : .02, 'high' : .5, 'very high' : 1}

# lookup table for overall risk likelihood based on likelihood of initiation (rows) and vulnerability (cols)
overall = {
    'very low' : {
        'very low' : 'very low',
        'low' : 'very low',
        'moderate' : 'low',
        'high' : 'low',
        'very high' : 'low'
    },
    'low' : {
        'very low' : 'very low',
        'low' : 'low',
        'moderate' : 'low',
        'high' : 'moderate',
        'very high' : 'moderate'
    },
    'moderate' : {
        'very low' : 'low',
        'low' : 'low',
        'moderate' : 'moderate',
        'high' : 'moderate',
        'very high' : 'high'
    },
    'high' : {
        'very low' : 'low',
        'low' : 'moderate',
        'moderate' : 'moderate',
        'high' : 'high',
        'very high' : 'very high'
    },
    'very high' : {
        'very low' : 'low',
        'low' : 'moderate',
        'moderate' : 'high',
        'high' : 'very high',
        'very high' : 'very high'
    },
}

# lookup table for risk level using overall likelihood (rows) and impact (columns
risk_level = {
    'very low' : {
        'very low' : 'very low',
        'low' : 'very low',
        'moderate' : 'very low',
        'high' : 'low',
        'very high' : 'low'
    },
    'low' : {
        'very low' : 'very low',
        'low' : 'low',
        'moderate' : 'low',
        'high' : 'low',
        'very high' : 'moderate'
    },
    'moderate' : {
        'very low' : 'very low',
        'low' : 'low',
        'moderate' : 'moderate',
        'high' : 'moderate',
        'very high' : 'high'
    },
    'high' : {
        'very low' : 'very low',
        'low' : 'low',
        'moderate' : 'moderate',
        'high' : 'high',
        'very high' : 'very high'
    },
    'very high' : {
        'very low' : 'very low',
        'low' : 'low',
        'moderate' : 'moderate',
        'high' : 'high',
        'very high' : 'very high'
    },
}
