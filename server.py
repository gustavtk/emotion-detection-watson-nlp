''' Executing this function initiates the application of emotion
    detection to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request

from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    ''' This code receives the text from the HTML interface and
        runs emotion detection over it using emotion_detector()
        function. The output returned shows the emotion scores and
        the dominant emotion for the provided text.
    '''
    # get the text that was typed in the page
    text_to_analyze = request.args.get('textToAnalyze')

    # run the emotion detection on it
    response = emotion_detector(text_to_analyze)

    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    # if dominant emotion is None the input was not valid (blank text)
    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    return "For the given statement, the system response is 'anger': {}, " \
           "'disgust': {}, 'fear': {}, 'joy': {} and 'sadness': {}. " \
           "The dominant emotion is <b>{}</b>.".format(
               anger, disgust, fear, joy, sadness, dominant_emotion)

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    # run the app on localhost port 5000
    app.run(host="0.0.0.0", port=5000)

