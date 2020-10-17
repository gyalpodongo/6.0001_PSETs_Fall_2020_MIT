## 6.0001 Pset 1: Part b
## Name: Gyalpo M Dongo Aguirre
## Time Spent: 1:00
## Collaborators: Edwin Ouko

#######################################################################################
## Get user input for salary, savings_percent, total_cost and raise_percentage below ##
#######################################################################################

salary = float(input("Enter your yearly salary: "))

savings_percent = float(input("Enter the percent of your salary to save, as a decimal: "))

total_cost = float(input("Enter the cost of your dream home: "))

raise_percentage = float(input("Enter the semi-annual raise, as a decimal: "))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################

percent_down_payment = 0.15

down_payment = total_cost*percent_down_payment

amount_saved = 0

r = 0.05

months = 0


###############################################################################################
## Determine how many months it would take to get the down payment for your dream home below ##
###############################################################################################

while amount_saved < down_payment:
    months += 1
    if months%6 == 0:
        #use of % to make sure when the months were a multiple of 6
        monthly_salary = salary/12
        monthly_savings = monthly_salary*savings_percent
        salary *= (1 + raise_percentage)
        #statement of salary put at the end as the alary was raised at the end
        #of the 6n month
    else:
        #use of else statements for other months not multiple of 6
        monthly_salary = salary/12
        monthly_savings = monthly_salary*savings_percent 
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