data = []
target = []
data_object_length = []
trained = False
def train(data_train, target_train):
#==========Checking types and lengths==========
  if type(data_train) == list:
    legal = True
    length = 0
    if type(data_train[0]) == list:
      length = len(data_train[0])
    else:
      legal = False
      raise Exception("Expected 2d array. 1d array provided.")
    for data_object in data_train:
      if type(data_object) == list:
        if len(data_object) != length:
          legal = False
          raise Exception("Inconsistent object lengths.")
      else:
        raise Exception("Expected 2d array. 1d array provided.")
        legal = False
  if type(target_train) == list:
    if legal == True:
      if len(data_train) != len(target_train):
        legal = False
        raise Exception("Inconsistent array lengths. Excpected: " + len(data_train) + ", " + len(data_train) + " Got: " + len(data_train) + ", " + len(target_train))
  else:
    legal = False
    raise Exception("Expected list (array). Got " + type(target_train))
  
#==========The functional part of this function=========
  if legal == True:
    global data
    data = data_train
    global target
    target = target_train
    global data_object_length
    data_object_length = len(data_train[0])
    global trained
    trained = True



def predict(data_new):
#==========Checking if new data has consistent formatting with training data=========
  legal = True
  if trained == True:
    if type(data_new) == list:
      if len(data_new) == 1:
        if type(data_new[0]) == list:
          if len(data_new[0]) != data_object_length:
            legal = False
            raise Exception("Inconsistent list (array) lengths. Expected: " + data_object_length + " Got: " + len(data_new[0]))
        else:
          legal = False
          raise Exception("Expected 2d array. Got 1d array.")
      else:
        legal = False
        raise Exception("Please keep array length to 1")
    else:
      legal = False
      raise Exception("Expected list (array). Got " + str(type(data_new)))
  else:
    legal = False
    raise Exception("Please train data first using train(training_data, training_target) function.")
  
#==========The functional part of the function==========
  if legal == True:
    highest_object = "Null"
    highest_score = "Null"
    for data_object in range(len(data)):
      score = 0
      for data_index in range(len(data[data_object])):
        score = score + abs(data_new[0][data_index] - data[data_object][data_index])

      if highest_score == "Null":
        highest_score = score
        highest_object = data_object
      
      if score < highest_score:
        highest_score = score
        highest_object = data_object
  return(target[highest_object])