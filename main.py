import knn
import json

#==========Opening data file and converting hex to decimal==========
rawData = open("data.json", "r")
data = json.loads(rawData.read())
for i in range(len(data["data"])):
  for color in range(len(data["data"][i])):
    data["data"][i][color] = int(data["data"][i][color], 16)
data_train = data["data"]
target_train = data["target"]
identifiers = data["identifiers"]

knn.train(data_train, target_train)

running = True
print("type exit to exit")
while running == True:
  predict = input("Input hex code:")
  if predict == "exit":
    break
 
  if len(predict) != 6:
    print("Please enter a six-digit color hex code.")
    continue
  part_1_predict = int(predict[:2], 16)
  part_2_predict = int(predict[2:4], 16)
  part_3_predict = int(predict[4:], 16)

  predict = [[part_1_predict, part_2_predict, part_3_predict]]

  prediction = knn.predict(predict)
  print("Predicted color: " + identifiers[prediction])