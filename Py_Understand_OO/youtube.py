
class youtube():
    def __init__(self,name,suscriber,video,suscribTo):
        self.name = name 
        self.suscriber = suscriber
        self.video = video
        self.suscribTo = suscribTo
    
user1 = youtube('UKantjadia',3,6,100)

print(user1.suscribTo)