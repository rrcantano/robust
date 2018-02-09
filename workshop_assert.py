##make an error if ins not true, otw continue
#assert True == False

#using a function
def mean(num_list):
    #add error warning, not python error
    assert len(num_list) != 0
    return sum(num_list)/len(num_list)



def mean2(num_list):
    if len(num_list) == 0:
        #if something wrong happens give a message
        raise Exception ("Connot compute the mean value of an empty lsit")
    else: 
        return sum(num_list)/len(num_list) 
     


def mean3(num_list):
    try:
       return sum(num_list)/len(num_list)
    except ZeroDivisionError as detail:
       #the message is writen in detail
       raise ZeroDivisionError(detail)


def mean4(num_list):
    try:
      mean = sum (num_list)/len(num_list)
      #check if 'mean' is of a certain type
      if isinstance(mean, complex):
          return NotImplemented
      return mean
    except ZeroDivisionError as detail:
      msg ="\nCannot compute the mean value of an empy list"
      raise ZeroDivisionError(detail.__str__() + msg)
    except TypeError as detail:
      msg = "\n Please pass a list of numbers not strings"
      raise ZeroDivisionError(detail.__str__() + msg)
