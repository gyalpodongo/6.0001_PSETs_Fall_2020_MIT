def part_c(starting_amount):
	#########################################################################
	house_cost = 750000
	down_payment_percentage = 0.25
	down_payment = house_cost*down_payment_percentage
	up_bound = 1.0
	low_bound = 0.0
	steps = 0
	r = 0.0
	number_of_months = 36
	epsilon = 100
	current_savings = starting_amount*(1+ (r/12))
	worst_case = starting_amount*(1+ (1/12))**number_of_months
	# worst_case is the case of the total current savings when r =1, so that
	# if when r = 1 and the worst_case is still smaller than the (down_payment - 100)
	# we will know that no matter what, the current_savings will never be close 
	# to down payment in 36 months
	
	
	########################################################################################################
	## Determine the lowest return on investment needed to get the down payment for your dream home below ##
	########################################################################################################
	
	if current_savings >=  (down_payment - epsilon) :
	    print("Best savings rate: {}".format(str(float(r))))
	    print("Steps in bisection search: {}".format(str(int(steps))))
	    # if current savings are already greater than (down_payment -100)
	    # no need to find a value for r
	elif  worst_case < (down_payment-epsilon):
	    r = None
	    # use of worst case  in case it is smaller than ((down_payment -100))
	    # if this condition is true, then no need of bisection search as we will
	    # know that the amount saved will  never be close to down_payment
	else:
	    while abs(current_savings - down_payment) > epsilon:
	        steps += 1
	        r = (up_bound+low_bound)/2
	        current_savings = starting_amount*(1+ (r/12))**number_of_months
	        if current_savings > down_payment:
	            up_bound = r
	            #if the current_savings are greater than down_payment, it means
	            #that the upper bound is too high so value of r is assigned to it
	        elif current_savings < down_payment:
	            low_bound = r
	            #if the current_savings are smaller than down_payment, it means
	            #that the lower bound is too low so value of r is assigned to it
	            
	
	##########################################################
	## Print out the best savings rate and steps taken here ##
	##########################################################
	print("Best savings rate: {}".format(r))
	print("Steps in bisection search: {}".format(str(steps)))
	return r, steps