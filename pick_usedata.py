import json
data_cleaned_num = 62
with open("./resource/manual_dataset.json",'r', encoding="utf-8") as f:
  data = json.load(f)

d_tuple=list(data.items())[:data_cleaned_num]
