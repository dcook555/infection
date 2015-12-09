import random

class Person:

     
     population=[]
     graveyard=[]
               

     def _init_(self):
         self.population.append(self)
         self.infected=False
         self.contagious=False

     def die(self):
         self.population.remove(self)
         self.graveyard.append(self)
         self.infected.remove(self)
     def tick (self):
          if self.infected:
               self.contagious = True
          if self.infected:
               self.die()
          if len (self.population) > 5
              freinds = random.sample(self.population,5)
          else:
            friends = self.population[:]
          for friend in friends:
               if friend.contagious:
                    self.infected=True
     
def create_people(self):
     patient_zero = person()
     patient_zero.infected=True
          
class DataWriter:
    '''A simple class to write data to a file.'''
    
    def __init__ (self, filecname):
        self.f = file(filename,'w')
        self.output_header()


        
    def output_text (self, txt):
        self.f.write(txt+'\n') # Add newline

    def output_list (self, data_list):
        txt = ''
        for itm in data_list:
            txt += str(itm)
        self.output_text(txt)
     def output_header (self):
        self.output_text('Live,Dead')

     def output_data (self):
        # Output data for our population...
        # You'll want to do something more so you can track the number
        # of infected people, immune people, etc.
        self.output_list([len(Person.population),len(Person.graveyard)])

     def finish (self):
        self.f.close()
def run_simulation (population, ticks, filename='data.csv'):
    dataWriter = DataWriter(filename)
    create_people(population)
    for t in range(ticks):
        dataWriter.output_data()
        for p in Person.population:
            p.tick()
    dataWriter.finish()
     print 'finish'
     

print'population:',len(Person.population)
p.die()
print'population:',len(Person.population),'alive',len(person.graveyard),'dead'
run_simulation(9000,360)
print "Done!"
