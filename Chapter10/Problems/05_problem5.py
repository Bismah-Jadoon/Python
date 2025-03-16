# Write a class Train which has methods to book a ticket, get status (no of seats) and get fare information of train running under Indian Railways.

from random import randint
class Train:
   
   def __init__(self, trainNo, fro, to):
       self.trainNo = trainNo
       self.fro = fro
       self.to = to
       
   
   def ticket(self):
       print(f"Ticket is booked in trainNo {self.trainNo} from {self.fro} to {self.to}")
   
   def status(self):
       print(f"The train with trainNo {self.trainNo} is running on time")
   
   def fare(self):
       print(f"Ticket fare in trainNo:  {self.trainNo} from {self.fro} to {self.to} is {randint(222,5555)}")

    
obj = Train(12,"Hyderabad", "Karachi")
obj.ticket()
obj.status()
obj.fare()