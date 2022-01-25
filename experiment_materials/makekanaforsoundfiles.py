import wanakana
import csv


def add_kana(file,column):
    
    romaji_dict={}
    with open("romajimappings.csv","r",encoding="UTF-8") as infile:
        reader=csv.DictReader(infile)
        for row in reader:
            letter=row["letter"]
            romaji=row["romaji"]
            romaji_dict[letter]=romaji
    infile.close()
            
    find_replace=[]
    for item in romaji_dict:
        if item!=romaji_dict[item]:
            find_replace.append((item,romaji_dict[item]))
            
            
    kana_list=[]
    with open(file,"r",encoding="UTF-8") as infile:
        reader=csv.DictReader(infile)
        for row in reader:
            forms=row[column].split("|")
            for form in forms:
                newform=form
                for item in find_replace:
                    newform=newform.replace(item[0],item[1])
                kana=wanakana.to_kana(newform)
                kana=kana.replace("q","っ")
                kana_list.append((form,kana))
    infile.close()

    with open("soundfiles.csv","w",encoding="UTF-8",newline="") as outfile:
        writer=csv.writer(outfile)
        for item in kana_list:
            writer.writerow(item)
    outfile.close()
            
