#defined functions to estimate population to be used in main prog. with paramentes _pop_change, _init_pop, _years inputted by the user
def estimate_population(_pop_change, _init_pop, _years):
    """
    #Use the population rate of change, initial population, and years to an estimated pop.
    :param _pop_change: rate that population is changing every year
    :param _init_pop: populationn at year 1
    :param _years: the number of year
    :return:
    """
    #inital population to add on to running total
    _total = _init_pop
    #the begin year of year 1
    i = 1
    #while function that continues until in inputted amount of years
    while i <= _years:
        #running total of each year
        _total = (_total + (_pop_change * _total))
        #year increment
        i = i + 1
    #add the end of the years print each parameter and estimate population to the nearest one person
    print("In", _years, "years, a populations of about", _init_pop, "people, with a growth rate of", _pop_change, "percent, the new pop. is estimated to be", round(_total, 0))

#using defined function in main prog with used inputted parameters
estimate_population(0.0111, 7.5e9, 3)
