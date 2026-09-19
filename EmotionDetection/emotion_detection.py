''' Emotion detection using the watson NLP library.
    Sends the text to the EmotionPredict service and returns the
    emotion scores plus the dominant emotion.
'''
import json
import requests


def emotion_detector(text_to_analyse):
    ''' this function takes the text from the user, sends it to the
        watson emotion detection service and returns a dict with the
        five emotion scores and the dominant emotion
    '''
    # url of the emotion predict service from the lab
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    # model id header, same one used in the labs
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    # the input has to be sent in this format
    myobj = {"raw_document": {"text": text_to_analyse}}

    # post the text to the service
    response = requests.post(url, json=myobj, headers=header, timeout=10)

    # when the text is blank the service gives a 400, so return None for everything
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None,
        }

    # turn the response text into a dict so we can work with it
    formatted_response = json.loads(response.text)

    # the scores we need are inside emotionPredictions -> emotion
    emotions = formatted_response['emotionPredictions'][0]['emotion']

    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    joy_score = emotions['joy']
    sadness_score = emotions['sadness']

    # the dominant emotion is just the one with the biggest score
    dominant_emotion = max(emotions, key=emotions.get)

    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion,
    }
