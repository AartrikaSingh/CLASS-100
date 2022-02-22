class Car(object):
    def __init__(self,company,color,speed) :
        self.company=company
        self.color=color
        self.speed=speed
    def start(self):
        print("Car Is Starting")
    def stop(self):
        print("Car Is Stoping")
    def acclerate(self):
        self.speed=self.speed+10
        print("Your Speed Of The Car Is:",self.speed)
car1=Car("Honda","Red",80)
car1.start()
car1.acclerate()
car1.stop()            
        
    