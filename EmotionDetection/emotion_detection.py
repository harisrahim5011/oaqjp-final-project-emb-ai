import requests, json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'  # URL of the sentiment analysis service
    myobj = { "raw_document": { "text": text_to_analyse } }  # Create a dictionary with the text to be analyzed
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}  # Set the headers required for the API request
    response = requests.post(url, json = myobj, headers=header)  # Send a POST request to the API with the text and headers
    format_res = json.loads(response.text)

    if response.status_code == 400: #or response.status_code == 500:
        return {
                    "anger": None, 
                    "disgust": None, 
                    "fear": None, 
                    "joy": None, 
                    "sadness": None, 
                    "dominant_emotion":None
                }
       
    emotion = format_res['emotionPredictions'][0]['emotion']
    emotion |= {'dominant_emotion': max(emotion, key=emotion.get)}
    return emotion
