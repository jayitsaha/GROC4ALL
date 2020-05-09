import os
import json
from os.path import join, dirname
from dotenv import load_dotenv
from ibm_watson  import SpeechToTextV1 as SpeechToText
# from watson_developer_cloud import AlchemyLanguageV1 as AlchemyLanguage
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import re
from speechText.speech_sentiment_python.recorder import Recorder
def transcribe_audio(path_to_audio_file):
    authenticator = IAMAuthenticator('hLItcSq3n1DJdH8SDHYxsLdn0MPpqLP8Wo30WO9Ea-OL')

    username = os.environ.get("BLUEMIX_USERNAME")
    password = os.environ.get("BLUEMIX_PASSWORD")
    speech_to_text = SpeechToText(authenticator=authenticator)
    speech_to_text.set_service_url('https://api.us-east.speech-to-text.watson.cloud.ibm.com/instances/f56cac90-ea6c-4c6e-a0d2-f6a07b9ce7e9')
    sstring = 'speechText'

    dir_path = os.path.dirname(os.path.realpath(__file__))
    print(dir_path)
    dir_path = dir_path.replace(sstring,'')

    with open(dir_path+"/speech.wav", 'rb') as audio_file:
        return speech_to_text.recognize(audio_file, content_type='audio/wav').get_result()
class Run():




    def main():
        recorder = Recorder("speech.wav")#
        print(recorder)

        print("Please say something nice into the microphone\n")
        recorder.record_to_file()

        print("Transcribing audio....\n")
        result = transcribe_audio('speech.wav')
        print(result)
        text = result["results"][0]["alternatives"][0]["transcript"]
        print(text)
        return text


    # if __name__ == '__main__':
    #     dotenv_path = join(dirname(__file__), '.env')
    #     load_dotenv(dotenv_path)
    #     try:
    #         main()
    #     except:
    #         print("IOError detected, restarting...")
    #         main()


