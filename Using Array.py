import numpy as np
import stocks
import scipy


# Convert each index list to an 1-D array
nasdaq = np.array(stocks.nasdaq)
sp500 = np.array(stocks.sp500)
djia = np.array(stocks.djia)
trading_days = np.array(stocks.trading_days)


# Find the mean of the index and divide the values in the area by the mean of 
#the index
#1
def percent_of_mean(input_list):
    input_array = np.array(input_list)
    mean_index = np.mean(input_list)
    index_as_percent = (input_array/mean_index)*100
    return index_as_percent

#2 find the percent of mean for all nasdaq, sp500, and djia. Ploted the percentage of all the indeices
import matplotlib.pyplot as plt

pofmean_nasdaq = percent_of_mean(nasdaq)
pofmean_sp500 = percent_of_mean(sp500)
pofmean_djia = percent_of_mean(djia) 
trades = stocks.trading_days #stocks of trading days into one variable

plt.figure("Indicies as percentages")
plt.title("Indices of POF Mean")
plt.plot (trades, pofmean_nasdaq, label = "nasdaq")
plt.legend()
plt.plot (trades, pofmean_sp500, label = "sp500")
plt.legend()
plt.plot (trades, pofmean_djia, label = "djia")
plt.legend(loc="best")
plt.xlabel("Trading Days")
plt.ylabel("Nasdaq, SP500, DJIA Indiceies")
plt.show()

#3
def num_days_big_per_chg(index_array, percent):
    number_days = 0
    percent_array1 = index_array[1:]
    percent_array2 = index_array[0:len(index_array)-1]
    per_difference = abs(percent_array1 - percent_array2) / percent_array2
    number_days = np.where(per_difference > percent)
    return np.size(number_days)
    
#4 I calculated the percent change of the stock indices, and put them ino bins
nasdaq_bins = [0, 0, 0, 0, 0] #bin sizes
sp500_bins = [0, 0, 0, 0, 0]
djia_bins = [0, 0, 0, 0, 0]

bins = [.002, .004, .006, .008, 0.01]

b = 0.002 #this bin checks for thestock of nasdaq of the tradings days and add it to the bin and increments by .002
    if num_days_big_per_chg(nasdaq, b):
        nasdaq_bins[i] += num_days_big_per_chg(nasdaq, b)
        b += 0.002
print(nasdaq_bins)

b = 0.002 #this bin checks for thestock of sp500 of the tradings days and add it to the bin and increments by .002
for i in range(np.size(bins)):
    if num_days_big_per_chg(sp500, b):
        sp500_bins[i] += num_days_big_per_chg(sp500, b)
        b += 0.002
print(sp500_bins)

b = 0.002
for i in range(np.size(bins)): #this bin checks for thestock of djia of the tradings days and add it to the bin and increments by .002
    if num_days_big_per_chg(djia, b):
        djia_bins[i] += num_days_big_per_chg(djia, b)
        b += 0.002
print(nasdaq_bins)
#graphs nasdaq, sp500, djia of the percent increase of the stocks indices and the number of days that greater than the previos day
plt.figure('Threshold Value')
plt.plot(bins, nasdaq_bins,\
'r--o', label="NASDAQ", markersize = 2)
plt.plot(bins, sp500_bins,\
'b--s', label="SP500", markersize = 2)
plt.plot(bins, djia_bins,\
'g--D', label="DJIA", markersize = 2)
plt.xlabel('Percentage Increase')
plt.ylabel('Days')
plt.title('Stocks Percentage Increases', size = 40.0)
plt.legend(loc= "best")
plt.savefig('stockspercentageincreases.png')
plt.show()
    
#5. the arrays of the percentage of the three
def moving_average(array):
   
    percent_change1 = index_array[2:]
    percent_change2 = index_array[1:-1]
    percent_change3 = index_array[:-2]
    moving_average = (percent_change1 + percent_change2 + percent_change3)/3
    return moving_average
    
#6 Using rh three simple movinf average for all the stock indices
#spereate graph versus the trading dats. That is the x-value
#y valueis the the stock indices

trading_moving = trading_days[3:]

nasdaq_ave = np.zeros(len(nasdaq) - 2, dtype = 'd')
nasdaq_ave.fill(scipy.mean(nasdaq))

plt.figure(3)
plt.plot(trading_moving, moving_average(nasdaq), linestyle='-', marker='o', label='Moving Average')
plt.plot(trading_moving, nasdaq_ave, linestyle='-', marker='D', label='Average')
plt.xlabel('Trading Days')
plt.ylabel('Nasdaq')
plt.title('Trading Days & Nasdaq', size=1.0)
plt.legend(loce="best")
#plt.savefig('Trading Days & NASDAQ'')
plt.show()

sp500_ave = np.zeros(len(sp500) - 2, dtype = 'd')
sp500_ave.fill(scipy.mean(sp500))



plt.figure(4)
plt.plot(trading_moving, moving_average(sp500), linestyle='-', marker='o', label='Moving Average')
plt.plot(trading_moving, sp500_ave, linestyle='-', marker='D', label='Average')
plt.xlabel('Trading Days')
plt.ylabel('Sq500')
plt.title('Trading Days & Sp500', size=1.0)
plt.legend(loce="best")
#plt.savefig('Trading Days & Sp500'')
plt.show()



djia_ave = np.zeros(len(djia) - 2, dtype = 'd')
djia_ave.fill(scipy.mean(djia))

plt.figure(4)
plt.plot(trading_moving, moving_average(djia), linestyle='-', marker='o', label='Moving Average')
plt.plot(trading_moving, djia_ave, linestyle='-', marker='D', label='Average')
plt.xlabel('Trading Days')
plt.ylabel('DJIA')
plt.title('Trading Days & DNJIA', size=1.0)
plt.legend(loce="best")
#plt.savefig('Trading Days & DJIA'')
plt.show()