#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 99.99% of work from other sources, including lesson 6 refresher jupyter notebook, python iii zoom videorecording, and JUL 03 2020 tutorial session with Ms. LT


# In[2]:


from pathlib import Path


# In[3]:


import csv


# In[28]:


csvpath = Path('02-Homework_02-Python_Instructions_PyBank_Resources_budget_data.csv') # problems in establishing path rectified by Instructor KS
dates = []
gains_and_losses = []
line_num = 0
with open(csvpath, 'r') as csvfile:
    
    # printing datatype of the file object
    # print(type(csvfile))
    
    # passing in the csv file to csv.reader() function (w ',' as delimiter) and return the csvreader object
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # printing csvreader datatype
    # print(type(csvreader))
    
    # skipping over header and iterating line_num by one
    header = next(csvreader)
    first_entry = next(csvreader) # extra use of Python 'next' method from Ms. LT
    line_num += 1
    # (firstentry)
    prev_profit_loss = int(first_entry[1]) 
    initial_entry = prev_profit_loss
    """ 
    having worked this out with the tutor, Ms. LT (on JUL 03, 2020) because of the nature of finding changes and the start for values of changes,
    there was the need to have the firstentry = next(csvreader) line and also the prev_profit_loss = int(first_entry[1]) line
    """
    #print(prevprofitloss)
    # printing header
    # print(f"{header}")
    delta = []
    # reading each row of data after the header
    # directly below in this cell except for the print (len...), my desired iterations
    # initial_difference = 
    # print(initial_difference)
    for row in csvreader:
        # print(row)
        date = (row[0])
        dates.append(date) # this line and line above adding for dates, exp_w_dates empty set established above
        gain_or_loss = int(row[1])
        gains_and_losses.append(gain_or_loss) # this line and line directly above adding for profit/losses, aggregate empty set established above
        change =  gain_or_loss - prev_profit_loss # structure of looping for values in change from Ms. LT
        delta.append(change)
        prev_profit_loss = gain_or_loss
        # in lines above, row are iterated so that a value change is calculated from difference of gain_or_loss and prev_profit_loss
        # gain_or_loss value is always being changed from iteration of row, prev_profit_loss is always being changed from definition of gain_or_loss
    total_number_of_months = len(dates) + line_num
    print(dates)
    print(gains_and_losses)
    print(delta)
    print(total_number_of_months)


# In[29]:


net_delta_aggregate = 0
for item in delta:
    net_delta_aggregate += item
average_delta = round(net_delta_aggregate/len(dates), 2)
print(average_delta)


# In[21]:


tally = 0 # idea for tally from Lesson 6 refresher notebook
for item in gains_and_losses:
    tally += item
print(tally)


# In[22]:


grand_total = tally + initial_entry


# In[23]:


print(grand_total)


# In[9]:


gain_maximum = 0
loss_maximum = 0


# In[10]:


for entry in delta: #structore of finding maximum and minimum from Lesson 6 refresher jupyter notebook
    if loss_maximum == 0:
        loss_maximum = entry
    if entry > gain_maximum:
        gain_maximum = entry
    elif entry < loss_maximum:
        loss_maximum = entry


# In[11]:


print(loss_maximum)


# In[12]:


print(gain_maximum)


# In[13]:


datemax = dates[delta.index(1926159)]


# In[14]:


datemin = dates[delta.index(-2196167)]


# In[32]:


print(datemax)
print(datemin)


# In[59]:


headline = "Financial Analysis"


# In[60]:


# saving 0020 EDT


# In[61]:


line_break = "----------------------------"


# In[62]:


output_path = Path('output.csv')


# In[63]:


with open(output_path, 'w'):
    print("Financial Analysis")
    print(line_break)
    print(f"Total: ${grand_total}")
    print(f"Average Change: ${average_delta}")
    print(f"Greatest Increase in Profits: {datemax} {gain_maximum}")
    print(f"Greatest Decrease in Profits: {datemin} {loss_maximum}")

07 06 2020 1800 EDT
# In[ ]:




