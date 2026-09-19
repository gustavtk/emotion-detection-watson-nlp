# Emotion Detection using Watson NLP

## Project Name
Emotion Detection Web Application - Final Project (Embeddable Watson AI)

## About
This is my final project for the course. It is a web app that takes customer
feedback as text and detects the emotion in it. Instead of just saying if the
feedback is positive or negative (sentiment analysis), it gives the scores for
five emotions: anger, disgust, fear, joy and sadness, and also tells which one
is the dominant emotion.

The app uses the embedded Watson NLP library (the EmotionPredict model) and is
deployed as a Flask web application on localhost:5000.

## Files
- `EmotionDetection/emotion_detection.py` - the emotion_detector function that calls the Watson NLP service
- `EmotionDetection/__init__.py` - makes EmotionDetection a package
- `server.py` - the Flask app with the /emotionDetector route
- `templates/index.html` and `static/mywebscript.js` - the web interface
- `test_emotion_detection.py` - unit tests for the app

## How to run
```
pip install flask requests
python3 server.py
```
Then open http://localhost:5000 in the browser, type some text and click
"Run Emotion Detection".

## Unit tests
```
python3 test_emotion_detection.py
```

## Static code analysis
```
pylint server.py
```
