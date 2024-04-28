#this program will take your net income and find a house by state that is in your budget.

#This takes the users anual net income
def user_income_and_state():
     user_income = int(input('Enter your annual net pay: '))
#This takes the users state
     user_state = input('Enter your state(LA, CA, FL, ETC.: ').upper()
     return user_income , user_state

def calculate_max_house(user_income, user_state):

#This is a list if all the states in the US
     states = ['AL','AZ','AR','CA','CO','CT','DE','DC']

#This is the dictionary of all the average housinh prices of each state.
     state_avg_price = {}

     state_avg_price['LA'] = 199091
     state_avg_price['CA'] = 974105
     state_avg_price['AL'] = 226045
     state_avg_price['AZ'] = 435000
     state_avg_price['AR'] = 256000
     state_avg_price['CO'] = 612000
     state_avg_price['CT'] = 387000
     state_avg_price['DE'] = 342000
     state_avg_price['DC'] = 626000


    #Finds the average price of house by state
     monthly_income = user_income / 12
     monthly_income *= .28
     monthly_income *= 12
     max_house = monthly_income * 30
     max_house = int(max_house)
         
     if user_state in state_avg_price:
          avg_price = state_avg_price[user_state]
        
    #calculates if max_house is < avg_price
    
          if max_house < avg_price:
               print(f"The average housing price in {user_state} is $ {avg_price}.")
               print("You cannot afford housing in this state")
          else:
    
               print('The average housing price in',user_state,'is $',avg_price,)
               print('\n')
               print('You can afford a $',max_house,'house')
def state_calc():
    
    while True:
        user_income, user_state = user_income_and_state()
        calculate_max_house(user_income, user_state)
        
        restart = input('Enter r to restart, or any other key to exit: ').upper()
        if restart != 'R':
            break

# Run the main function
state_calc()
    
    
    
    
    



    