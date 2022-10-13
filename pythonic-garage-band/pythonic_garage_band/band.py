from abc import ABC , abstractclassmethod, abstractmethod



        


class Musician(ABC):
    
    '''
     An abstract class that contains instance attribute name and abstract methods:
        1. __str__
        2. __repr__
        3. get_instrument
        4. play_solo
     
  
     '''

  
    def __init__(self, name):
        self.name = name
    @abstractmethod
    def __str__(self) :
        pass
    @abstractmethod 
    def __repr__(self) :
        pass
    @abstractclassmethod
    def get_instrument(self):
        pass
    @abstractclassmethod
    def play_solo(self):
        pass



class Band(Musician):

   
    ''' 
      A child classthat contains:
        1. instance attributes "name and members"
        2. class method "to_list"
        3. class attribute "instances" which is a list of instances that inherit from base class.
        4."play_solos" method that asks each member musician to play a solo.
        5. abstracted methods from parent class
     
     '''


    instances =[]
   
    def __init__(self,name,members=[] ) :
        super().__init__(name)
        self.name =name
        self.members=members
        Band.instances.append(self)
    def play_solos(self):
        music_solo=[]
        for x in self.members:

             music_solo.append(x.play_solo())
        return music_solo
    def play_solo(self):
    
        pass      

    def get_instrument(self):
        pass 
    @classmethod
    def to_list(cls):
        return Band.instances
    def __str__(self) :
        return self.name
    def __repr__(self):
        return self.name

class Guitarist(Musician):
    '''
    A child class that contains instance attribute name and abstracted methods:
        1. __str__
        2. __repr__
        3. get_instrument
        4. play_solo
    from parent class(Musician)
    '''

    def __init__(self, name):
        self.name = name
        super().__init__(name)
    def __str__(self) :
        return f"My name is {self.name} and I play guitar"
    def __repr__(self) :
        return f"Guitarist instance. Name = {self.name}"
    def play_solo(self):
        return "face melting guitar solo"
    def get_instrument(self):
        return "guitar"

class Drummer(Musician):

    '''
    A child class that contains instance attribute name and abstracted methods:
        1. __str__
        2. __repr__
        3. get_instrument
        4. play_solo
    from parent class(Musician)
    '''

    def __init__(self, name):
        super().__init__(name)
        self.name=name 

    def __str__(self) :
        return f"My name is {self.name} and I play drums"
    def __repr__(self) :
        return f"Drummer instance. Name = {self.name}"
    def play_solo(self):
        return "rattle boom crash"
    def get_instrument(self):
        return "drums"

class Bassist(Musician):

    '''
    A child class that contains instance attribute name and abstracted methods:
        1. __str__
        2. __repr__
        3. get_instrument
        4. play_solo
    from parent class(Musician)
    '''
   
    def __init__(self, name):
        super().__init__(name)
        self.name=name
    def __str__(self):
        return f"My name is {self.name} and I play bass"
    def __repr__(self):
        return f"Bassist instance. Name = {self.name}"

    def play_solo(self):
        return "bom bom buh bom"
    def get_instrument(self):
        return "bass"
