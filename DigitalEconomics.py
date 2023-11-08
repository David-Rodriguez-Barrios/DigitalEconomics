#ENDG 233 final project
#By:
#   Dawson van Vlaanderen
#   David Rodriguez
#Group 2 Pairs Block 4
#this project uses Pandas along with numpy and matplotlib

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class Company:
    """A class used to create a Company object.

        Attributes:
            array : array of the company's stock data
            name : String that represents the company's name
            initial_date_index : integer that represents the index of the user's chosen initial date in the company's array
            final_date_index : integer that represents the index of the user's chosen fin al date in the company's array

    """
    def __init__(self, data, name):
        self.array = data
        self.name = name
        self.initial_date_index = 0
        self.final_date_index = 0

    def minimum_value(self):
        """ Finds the minimum value of stock price between the initial and final date. Using the minimum stock price value for every day given in the CSV file.

        Arguments: self-variables from the constructor (the self.array: array of the company instance, self.initial_date_index (index of the initial date chosen by user), and self.final_date_index (index of the final date chosen by user) are the variables used in this functon)
        Returns: the lowest value of the stock price between the initial and final date and the date it occurred (by using the minimum stock price for every day in between)
        
        """
        minimum = np.min(self.array[self.initial_date_index: self.final_date_index + 1, 3]) # the minimum value
    
        row_with_min_value = 0 #sets the variable to search for row that the minimum value occured
        while minimum != self.array[row_with_min_value, 3]: # while the minimum value does not equal  the minimum value reported on row x in the array:
            row_with_min_value += 1 #increment the row by 1
        date = self.array[row_with_min_value, 0] # the date is equal to the row that the minimum value is at the zero index
        return('{:.2f}$ on {}'.format(minimum, date)) # gives the lowest minimum value reported for each day between the initial and final date and the date that it occured on.

    def maximum_value(self):
        """ Finds the maximum value of stock price between the initial and final date. Using the maximum stock price value for every day given in the CSV file.

        Arguments: self-variables from the constructor (the self.array: array of the company instance, self.initial_date_index (index of the initial date chosen by user), and self.final_date_index (index of the final date chosen by user) are the variables used in this functon)
        Returns: the highest value of the stock price between the initial and final date (by using the greatest stock price reported for every day in between)

        """
        maximum = np.max(self.array[self.initial_date_index: self.final_date_index + 1, 2]) # the maximum value
    
        row_with_max_value = 0 #sets the variable to search for row that the maximum value occured
        while maximum != self.array[row_with_max_value, 2]: # while the maximum value does not equal  the maximum value reported on row x in the array:
            row_with_max_value += 1 #increment the row by 1
        date = self.array[row_with_max_value, 0] # the date is equal to the row that the maximum value is at the zero index
    
        return('{:.2f}$ on {}'.format(maximum, date)) # gives the highest maximum value reported for each day between the initial and final date and the date that it occured on.

    def percent_change(self, percent_yes = True):
        """ A function that calculates the percent change of the stock between two dates given in the companie's array, inital date, and final date.

        Parameters: percent_yes: determins whether to return the net change in stock price between the user's chosen dates or the percent change between the user's chosen dates through the equation: (initial - final) / initial * 100 
                    self-variables from the constructor (the self.array: array of the company instance, self.initial_date_index (index of the initial date chosen by user), and self.final_date_index (index of the final date chosen by user) are the variables used in this functon)
        Returns: the Percent change or the net change in stock prices between the two chsen dates

        """
        initial_price = float(self.array[self.initial_date_index][4]) #Gives the initial price by using the row found above and index 4 containg the close stock price
        final_price = float(self.array[self.final_date_index][4]) #Gives the final price of the stock at close on the final date
        if percent_yes:
            return ('{:.2f}%'.format((final_price - initial_price) / initial_price * 100)) #the function will return the percent change of the price between the initial price and the final price
        else: return ('{:.2f}$'.format(final_price - initial_price))

    def day_to_day_change(self, extreme, return_list = False):
        """ finds the biggest increase and decrease (change) in stock price between one day and the next, both of which are chosen by the user

        Parameters: extreme: when the function is called, if extreme is set to increase, the function will calculate the biggest increase withen the chosen dates or if extreme is given the value decrease, it will make the function find the biggest increase withen the chosen dates
                    self-variables from the constructor (the self.array: array of the company instance, self.initial_date_index (index of the initial date chosen by user), and self.final_date_index (index of the final date chosen by user) are the variables used in this functon)
                    return_list: makes it so the function returns a dictionary of the day change as key and there index as value if needed
        Returns:  the biggest increase and decrease (change) in stock price between one day and the next
                  or a list containing all the changes for the day if return_list is ture

        """
        list_of_values = [self.array[i + 1][4] - self.array[i][4] for i in range(self.initial_date_index, self.final_date_index)] #makes a list containing the values of the the changes in stock price between a day and the next adjacent day as keys
        list_of_indexs = [i for i in range(self.initial_date_index, self.final_date_index + 1)]#makes a list containing the indexs of the values, for every day in the user's chosen range that has a day afetr it(so not including the final day included, since it doesnt look at the day after the final one)
        if return_list == False:
            if extreme == 'increase':
                value = np.max(np.array(list_of_values)) #finds the highest value in the value list if extream is "increase"
            elif extreme == 'decrease':
                value = np.min(np.array(list_of_values)) #finds the lowest value in the value list if extream is "decrease"
            return '{:.2f}$ which happens during {}'.format(value, self.array[list_of_indexs[list_of_values.index(value)] + 1][0]) # returns the biggest increase/decrease between the chosen dates as a string with the corresponding adjacent dates
        else: return list_of_values #returns the list of the day to day change values

    def list_of_all_days(self, info_of_months):
        """ finds a list of all the days between the first and the last in the data array including weekends holidays

        Parameters: info_of_months: array containing the months by number and the number of days in each month
        Returns: it returns a list of all the days between the first and the last in the data array including weekends holydays

        """

        initial_date_list = [int(i) for i in self.array[0][0].split('-')] #turns the first day in the array into a list and makes the values integers
        final_date_list = [int(i) for i in self.array[-1][0].split('-')] #turns the last day in the array into a list and makes the values intergers

        months = dict([(int(i[0]), int(i[1])) for i in info_of_months]) #makes a dictionary with the months(as numbers) as the keys and the number of days in each month being the value
        
        list_of_days = [] #list to hold all of the days between the first and last day in the array

        list_of_days.append('-'.join([str(initial_date_list[0]), str(initial_date_list[1]).zfill(2), str(initial_date_list[2]).zfill(2)]))

        #loops over untill the in date becomes the final date, 
        while (initial_date_list != final_date_list):
            #checks to see if the year that it is currently counting in is a leapyear and ajusts the february days acordingly
            if initial_date_list[0] % 4 == 0:
                months[2] = 29
            else: months[2] = 28
            #every loop, the separation_days increases, if the days is the same value as the days in the month it is currently working with, it jumps to the next month and sets the days to 1, else it will just increase the days by one
            #when jumping to the next month, if the months are at 12 (december), it changes the months back to 1 (january) and increases the year by one, else it will increase the months by one
            if(initial_date_list[2] == months[initial_date_list[1]]):
                initial_date_list[2] = 1
                if(initial_date_list[1] == 12):
                    initial_date_list[1] = 1
                    initial_date_list[0] += 1
                else:
                    initial_date_list[1] += 1
            else:
                initial_date_list[2] += 1
            list_of_days.append('-'.join([str(initial_date_list[0]), str(initial_date_list[1]).zfill(2), str(initial_date_list[2]).zfill(2)]))
        return list_of_days

def day_count(initial_date, final_date, info_of_months):
    """ finds out how many  days are in between the two user selected days

    Parameters: initial_date: the initial date chosen by the user
                final_date: the final date chosen by the user
                info_of_months: array containing the months by number and the number of days in each month
    Returns: it returns the days between the user's chosen days

    """

    initial_date_list = [int(i) for i in initial_date.split('-')] #turns the initial day into a list and makes the values integers
    final_date_list = [int(i) for i in final_date.split('-')] #turns the final day into a list and makes the values integers

    months = dict([(int(i[0]), int(i[1])) for i in info_of_months]) #makes a dictionary with the months(as numbers) as the keys and the number of days in each month being the value
    
    separation_days = 0 #variable to keep track of the  number of days in between the dates

    #loops over untill the in date becomes the final date, 
    while (initial_date_list != final_date_list):
        #checks to see if the year that it is currently counting in is a leapyear and adjusts the February days acordingly
        if initial_date_list[0] % 4 == 0:
            months[2] = 29
        else: months[2] = 28
        #every loop, the separation_days increases, if the days is the same value as the days in the month it is currently working with, it jumps to the next month and sets the days to 1, else it will just increase the days by one
        #when jumping to the next month, if the months are at 12 (december), it cahnges the months back to 1 (january) and increases the year by one, else it will increas the months by one
        #because of checks that happen before this function is called, the initial date should come before the final date and they both should be acceptable values 
        if(initial_date_list[2] == months[initial_date_list[1]]):
            initial_date_list[2] = 1
            if(initial_date_list[1] == 12):
                initial_date_list[1] = 1
                initial_date_list[0] += 1
            else:
                initial_date_list[1] += 1
        else:
            initial_date_list[2] += 1
        separation_days += 1
    return separation_days      

def where_the_ticks_are(initial_date_index, final_date_index, num_of_ticks):
    """ finds where the ticks should be on the graph so they are still evenly separated through the x axis, no mater how many days are within the days chosen by the user

    Parameters: initial_date: the initial date chosen by the user
                final_date: the final date chosen by the user
                num_of_ticks: how many ticks should apear on the graph
    Returns: it returns a list of the indexs of each tick for the graph

    """
    ticks_index = []
    list_of_indexs = list(range(initial_date_index, final_date_index + 1)) #list of the indexs between the initial and final dates indexs
    num_of_days = len(list_of_indexs) #number of days between the two chosen days
    #if there are more ticks wanted then there are days between the chosen dates, it will change the ticks to be less(ticks = amount of days)
    if num_of_days <= num_of_ticks:
        return list_of_indexs
    else:
        days_between_ticks = num_of_days//num_of_ticks #splits up the days by the amout of ticks wanted
        before_after = ((num_of_days % num_of_ticks) + (days_between_ticks - 1)) // 2 #adds half of the begginging amout of day to half of the remainder days to make an even spacing before the first tick and after the second
        #deletes the indexs before the first tick
        while before_after > 0:
            del list_of_indexs[0]
            before_after -= 1
        #starts with setting the first value (after the ones that got taken away) in a list, then goes throught the list of indexes. After the checker amount, which is the number of days between ticks, after it passes that many, it places another tick index into the list
        checker = int(days_between_ticks)
        for i in list_of_indexs:
            if days_between_ticks == checker and len(ticks_index) < num_of_ticks:
                days_between_ticks = 1
                ticks_index.append(i)
            else: days_between_ticks += 1
        return ticks_index
    


def main():
    #data from November 28 2016 to November 28 2021
    #no data for weekends, holidays and govermental shut down periods

    #importing the csv files needed for the project
    amazon = pd.read_csv('AMZN.csv', delimiter=',')
    google = pd.read_csv('GOOG.csv', delimiter=',')
    netflix = pd.read_csv('NFLX.csv', delimiter=',')
    facebook = pd.read_csv('FB.csv', delimiter=',')
    apple = pd.read_csv('AAPL.csv', delimiter=',')
    monthly_info = pd.read_csv('Months_and_days_in_Months.csv', delimiter=',')
    accepted_companies = pd.read_csv('accepted_companies.csv', delimiter=',')

    #converting the files to numpy arrays
    amazon = amazon.to_numpy()
    google = google.to_numpy()
    netflix = netflix.to_numpy()
    facebook = facebook.to_numpy()
    apple = apple.to_numpy()
    monthly_info = monthly_info.to_numpy()
    accepted_companies = accepted_companies.to_numpy()

    print('\nWELCOME\nTo the past stock price checker\n-Digital Economics-\n-------------------\n')

    #accepts the users input on what company they would want to see the information on, if it is not one of the choises, it will keep asking again
    while True:
        print('Companies available to receive information on:\n\t- Amazon\n\t- Apple\n\t- Facebook\n\t- Google\n\t- Netflix')
        user_input = input('Which one would you like to know the stock information on?:\n').lower()
        if (user_input in accepted_companies):
            print('-------------------------\nCompany was accepted\n-------------------------')
            break
        else:print('\nCompany was not accepted\nplease try again\n')

    #based creats an instance of the Company Class depending on which business the user picked
    if(user_input == accepted_companies[0]):
        the_company = Company(amazon, 'amazon'.capitalize())
    elif(user_input == accepted_companies[1]):
        the_company = Company(apple, 'apple'.capitalize())
    elif(user_input == accepted_companies[2]):
        the_company = Company(facebook, 'facebook'.capitalize())
    elif(user_input == accepted_companies[3]):
        the_company = Company(google, 'google'.capitalize())
    elif(user_input == accepted_companies[4]):
        the_company = Company(netflix, 'netflix'.capitalize())  

    #list of days that are accepted in the data array in the format YYYY-MM-DD
    accepted_dates = [i[0] for i in the_company.array]

    #list of days that are accepted in between the first and last date in the company's array in the format YYYY-MM-DD
    all_days_in_5_years = the_company.list_of_all_days(monthly_info)

    print('\n\nThe stock market is shut down on weekends, holidays and on days that the government shuts it down.\nBecause of this, these days dont have information and should be avoided when selecting initial and final dates.\n')
    print('What time period do you want to know the stock information on for ' + user_input.capitalize() + '?\nplease try to keep the dates a minimum of 10 days apart and between between November 28 2016 (2016-11-28) and November 26 2021 (2021-11-26)')
    #input checker for the dates Please type in dates between November 28 2016 (2016-11-28) and November 26 2016 (2016-11-26) while following the 3 ruels abouve about stock market shut down.
    while True: #input checker for the dates

        #checks if the initial date is a valid on. it is valide if the date is within the date range November 28 2016(2016-11-28) and November 26 2016(2016-11-26) and is not a weekend, holiday or a government shut down day
        while True:
            initial_date = input('\nPlease input the inital date as YYYY-MM-DD separated with a dash\nIf the date inputed is a weekend, holiday or a government shut down day, it will be rounded down\n(EX: 2018-03-12 is March 12, 2018):\n')
            #makes the inpup into the proper format of YYYY_MM_DD if the day or month are inputed ans a single diget
            if(initial_date.count('-') == 2):
                pass
                initial_date = initial_date.split('-')
                initial_date = '-'.join([initial_date[0], initial_date[1].zfill(2), initial_date[2].zfill(2)])
                #brings the date down one untill it reaches one that has data in the company's array
                while initial_date in all_days_in_5_years and initial_date not in accepted_dates:
                    initial_date = all_days_in_5_years[all_days_in_5_years.index(initial_date) - 1]
                if initial_date in accepted_dates:
                    print('-------------------------\nInitial date was accepted\n-------------------------\n')
                    break
                else: print('Initial date was not accepted\ndate inputed is not between November 28 2016 and November 26 2021\nplease try again')
            else: print('\nplease make sure your date follows the YYYY-MM-DD format')

        #checks if the final date is a valid on. it is valid if the date is within the date range November 28 2016(2016-11-28) and November 28 2016(2016-11-28) and is not a weekend, holiday or a government shut down day
        while True: 
            final_date = input('\nPlease input the final date as year-month-day separated with a dash\nIf the date inputed is a weekend, holiday or a government shut down day, it will be rounded down\n(EX: 2019-07-02 is July 2, 2019):\n')
            #makes the input into the proper format of YYYY_MM_DD if the day or month are inputed ans a single diget
            if (final_date.count('-') == 2):
                pass
                final_date = final_date.split('-')
                final_date = '-'.join([final_date[0], final_date[1].zfill(2), final_date[2].zfill(2)])
                #brings the date down one until it reaches one that has data in the company's array
                while final_date in all_days_in_5_years and final_date not in accepted_dates:
                    final_date = all_days_in_5_years[all_days_in_5_years.index(final_date) - 1]
                if final_date in accepted_dates:
                    print('-------------------------\nFinal date was accepted\n-------------------------\n\n')
                    break
                else: print('Final date was not accepted\ndate inputed is not between November 28 2016 and November 26 2021\nplease try again')
            else: print('\nplease make sure your date follows the YYYY-MM-DD format')

        # checks if the final date comes before the initial date 
        if accepted_dates.index(initial_date) >= accepted_dates.index(final_date):
            print('initial date inputted occures after the final date inputted\nplease try the dates again')  #informs the user that their final date occurs before their initial date
        else: break # if the dates are fine then the loop breaks

    the_company.initial_date_index = 0
    while the_company.array[the_company.initial_date_index][0] != initial_date: #while the date of the company array at that row is not equal to the initial date:
        the_company.initial_date_index +=1 #add one to the row

    the_company.final_date_index = 0
    while the_company.array[the_company.final_date_index][0]  != final_date: #while the date of the company array at that row is not equal to the initial date:
        the_company.final_date_index += 1 #adds one to the row2
    
    #prints out all the calculated and found data for the user
    print('\n\t- Num of days within chosen dates: ' + str(day_count(initial_date, final_date, monthly_info))) # prints the time elapsed within the dates
    print('\t- Direct change within chosen dates(stock price at close): ' + the_company.percent_change(False)) # prints the direct change between those two days
    print('\t- Percent change within chosen dates(stock price at close): ' + the_company.percent_change()) # prints the percent change between those days
    print('\t- Highest priced stock within chosen dates(using maximum reported values): ' + the_company.maximum_value()) #prints the highest price recorded for that stock between the dates 
    print('\t- Lowest priced stock within chosen dates (using minimum reported values): ' + the_company.minimum_value()) #prints the lowest price recorded for that stock
    print('\t- Biggest increase in stock price during one active day within chosen dates(using stock price at close): ' + the_company.day_to_day_change('increase')) #prints the largest increase between two days for the stock price
    print('\t- Biggest decrease in stock price during one active day within chosen dates(using stock price at close): ' + the_company.day_to_day_change('decrease')) #prints the largest decrease between two days for the stock price

    market_cap_array = the_company.array # creates an array to manipulate the array with 
    w=0 #an integer that will be used later on as an index in the for loop
    for i in market_cap_array[the_company.initial_date_index:the_company.final_date_index,6]: #for every volume number in the company array:
        market_cap_array[the_company.initial_date_index:the_company.final_date_index,6][w] = market_cap_array[the_company.initial_date_index:the_company.final_date_index,4][w]*market_cap_array[the_company.initial_date_index:the_company.final_date_index,6][w] #the new number there is the volume for that date times the stock price at close for that date
        w+=1 #increments the index by one

    #makes and stiles the first plot that shows the stock prices throught the days selected
    fig, ax1 = plt.subplots(figsize = (10,6)) # creates a figure as a subplot with a figure size of 10 and 6
    plt.plot(range(the_company.initial_date_index,the_company.final_date_index + 1),the_company.array[the_company.initial_date_index:the_company.final_date_index + 1,4],'r--',label = 'Stock Price at Close') #plots the dates along the x axis and the stock price along the y axis
    plt.plot(range(the_company.initial_date_index,the_company.final_date_index + 1),the_company.array[the_company.initial_date_index:the_company.final_date_index + 1,2],'b--',label = 'Highest stock price recorded on that day', alpha = 0.25)
    plt.plot(range(the_company.initial_date_index,the_company.final_date_index + 1),the_company.array[the_company.initial_date_index:the_company.final_date_index + 1,3],'g--',label = 'Lowest stock price recorded on that day',alpha = 0.25)
    plt.ylabel('Stock Price in USD') #labels the y axis as market cap in USD
    plt.xlabel('Date') #labels the x axis as dates
    tick_index = where_the_ticks_are(the_company.initial_date_index, the_company.final_date_index, 5) #shows where the ticks are along the graph and how many (5)
    ax1.set_xticks(tick_index, [the_company.array[i][0] for i in tick_index]) # gives the date to that corresponding tick index
    plt.title('Stock price for {} within {} and {}'.format (user_input,initial_date, final_date)) # prints a title called "Stock price" and specificies the dates
    plt.legend(shadow = True, loc = 'upper left') # creates a legend at the upper left corner

    fig, ax2 = plt.subplots(figsize = (10,6)) 
    plt.plot(range(the_company.initial_date_index, the_company.final_date_index), list(the_company.day_to_day_change('increase',True)),'y--', label = 'Daily Stock price Change') #plots the date as the x axis and the market capitilization value calculated previously as the y.
    plt.ylabel('Daily Stock price change') #labels the y axis as market cap in USD
    plt.xlabel('Date') #labels the x axis as dates
    tick_index = where_the_ticks_are(the_company.initial_date_index, the_company.final_date_index, 5) #shows where the ticks are along the graph and how many (5)
    ax2.set_xticks(tick_index, [the_company.array[i][0] for i in tick_index]) # gives the date to that corresponding tick index
    plt.title('Market capitalization for {} within {} and {}'.format (user_input,initial_date, final_date)) # prints a title called "market capitlization" and specificies the dates
    plt.legend(shadow = True, loc = 'upper left') # creates a legend at the upper left corner

    fig, ax3 = plt.subplots(figsize = (10,6)) 
    plt.plot(range(the_company.initial_date_index, the_company.final_date_index + 1),market_cap_array[the_company.initial_date_index:the_company.final_date_index + 1,6],'b--', label = 'Market Cap') #plots the date as the x axis and the market capitilization value calculated previously as the y.
    plt.ylabel('Market Cap in USD') #labels the y axis as market cap in USD
    plt.xlabel('Date') #labels the x axis as dates
    tick_index = where_the_ticks_are(the_company.initial_date_index, the_company.final_date_index, 5) #shows where the ticks are along the graph and how many (5)
    ax3.set_xticks(tick_index, [the_company.array[i][0] for i in tick_index]) # gives the date to that corresponding tick index
    plt.title('Market capitalization for {} within {} and {}'.format (user_input,initial_date, final_date)) # prints a title called "market capitlization" and specificies the dates
    plt.legend(shadow = True, loc = 'upper left') # creates a legend at the upper left corner

    plt.show() # shows the graphs

if __name__ == '__main__':
    main()