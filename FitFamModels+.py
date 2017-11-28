
# coding: utf-8

# In[29]:

from datetime import datetime


# In[12]:

class Event:
    def __init__(self,name,description, startdate, enddate):
        self.name = name
        self.description = description
        self.startdate = startdate 
        self.enddate = enddate 
   
        

        


# In[13]:

class User:
    def __init__(self,username):
        self.username = username
        


# In[ ]:




# In[14]:

class Activity:
    def __init__(self,distance,description,timeOfDay,actDate, goal):
        self.distance = distance 
        self.description = description
        self.timeofDay = timeOfDay
        self.actDate = actDate 
        goal.addActivity(self)


# In[21]:

class Goal:
    def __init__(self,distanceGoal,event,user):
        self.complete = False
        self.distanceGoal = distanceGoal
        self.remaining = distanceGoal
        self.event = event 
        self.user = user
        self.activities = []
    def addActivity(self,activity):
        self.activities.append(activity)
        self.remaining -= activity.distance
        if self.remaining <= 0:
            self.complete = True 
            self.remaining = 0 
            print("Congratulations you have completed your goal!")
    
        


# In[45]:

user1 =  User("Jon")


# In[46]:

event1 = Event("Turkey Trot 2017", "Run 10k in November", datetime(2017, 11, 24) , datetime(2017,11, 27))


# In[47]:

goal1=Goal(10,event1,user1)


# In[48]:

activity = Activity(5,"Quick Jog","Morining",datetime(2017, 11, 24),goal1)


# In[49]:

print(goal1.__dict__)


# In[50]:

activity1 = Activity(5,"Great workout","Afternoon",datetime(2017, 11, 25),goal1)


# In[51]:

print(goal1.__dict__)


# In[ ]:



