import chardet
import json
with open("./resource/natori_taiwa.wav_transcript.txt", 'r',encoding="utf-8") as f:
  raw_data = f.read()
# len(raw_data_list)=231
raw_data_list = raw_data.split("\n")
del_blank_raw_data = [x for x in raw_data_list if x != ""]
times = []
texts = []
for i in range(len(del_blank_raw_data)):
  d = del_blank_raw_data[i]
  if d[0]=="S" or d[0]=="{":
    times.append(d)
  elif d == " ---   End of transcript   --- ":
    pass
  elif len(times)==len(texts):
    text_list = d.split(" ")
    kanzi_hiragana_list = [x.split("|")[0] for x in text_list]
    texts[-1] = texts[-1]+ "".join(kanzi_hiragana_list)
  else:
    text_list = d.split(" ")
    kanzi_hiragana_list = [x.split("|")[0] for x in text_list]
    texts.append("".join(kanzi_hiragana_list))
dict_text = dict(zip(times,texts))
with open("./resource/natori_taiwa_clean.json","w",encoding='utf-8') as f:
  json.dump(dict_text,f,ensure_ascii=False,indent="")