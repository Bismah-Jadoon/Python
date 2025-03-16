# Can you change the self-parameter inside a class to something else. Try changing self to "slf"  and see the effects.
# No, nothing will happen.We just use self to increase readability
from random import randint
class Train:
   
   def __init__(slf, trainNo, fro, to):
       slf.trainNo = trainNo
       slf.fro = fro
       slf.to = to
       
   
   def ticket(slf):
       print(f"Ticket is booked in trainNo {slf.trainNo} from {slf.fro} to {slf.to}")
   
   def status(slf):
       print(f"The train with trainNo {slf.trainNo} is running on time")
   
   def fare(slf):
       print(f"Ticket fare in trainNo:  {slf.trainNo} from {slf.fro} to {slf.to} is {randint(222,5555)}")

    
obj = Train(12,"Hyderabad", "Karachi")
obj.ticket()
obj.status()
obj.fare()