# make the sound files
import csv
import os
from google.cloud import texttospeech
from google.oauth2 import service_account

# you need a file soundfiles.csv which has the kana in the first column, and the romaji in the second column.
# This script will then generate mp3 sound files of those files. You can change it to wav or something else if you want

## ! REPLACE WITH THE PATH TO THE CREDENTIALS FOR YOUR OWN GOOGLE CLOUD ACCOUNT (probably in a similar location)
pathtokey='C:\\Users\\bonmc643\\AppData\\Local\\Google\\Cloud SDK\\bonniekey.json'

credentials = service_account.Credentials.from_service_account_file(pathtokey)


def synthesise(kana,romaji):
    client=texttospeech.TextToSpeechClient(credentials=credentials)
    input_text = texttospeech.SynthesisInput(text=kana)
    voice = texttospeech.VoiceSelectionParams(
            language_code="ja-JP",
            name="ja-JP-Wavenet-B",
            ssml_gender=texttospeech.SsmlVoiceGender.FEMALE,
        )

    audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.MP3
        )

    response = client.synthesize_speech(
            request={"input": input_text, "voice": voice, "audio_config": audio_config}
        )

    directory=os.path.abspath(os.getcwd())
    path=directory+'\\soundfiles\\'
    
    outfile=path+romaji+'.mp3'
    with open(outfile, "wb") as out:
        out.write(response.audio_content)

soundfiles=[]
with open('soundfiles.csv','r',encoding='utf-8') as infile:
    reader=csv.reader(infile)
    for row in reader:
        soundfiles.append(row)
        
for pair in soundfiles:
    synthesise(pair[1],pair[0])
