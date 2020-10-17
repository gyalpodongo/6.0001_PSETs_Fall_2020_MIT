def part_a(salary, savings_percent, total_cost):
	#########################################################################
	
	percent_down_payment = 0.15
	
	down_payment = total_cost*percent_down_payment
	
	monthly_salary = salary/12
	
	monthly_savings = monthly_salary*savings_percent
	
	amount_saved = 0
	
	r = 0.05
	
	months = 0
	
	###############################################################################################
	## Determine how many months it would take to get the down payment for your dream home below ##
	###############################################################################################
	
	while amount_saved < down_payment:
	    #while loop will keep on running until condition is no longer met
	    months += 1
	    #formula for amount_saved 
	    # Cn is the amount_saved in month n
	    # Cn+1 = Cn + monthly_savings + (r*Cn)/12
	    #(r*Cn)/12 is the monthly rate of return in amount_saved
	    # Cn+1 = Cn(1 + r/12) + monthly_savings
	    amount_saved += monthly_savings
	    amount_saved*= (1+ (r/12))
	
	
	    
	
	#######################################################
	## Print out the number of months it would take here ##
	#######################################################
	
	print("Number of months: {}".format(str(months)))
	return months