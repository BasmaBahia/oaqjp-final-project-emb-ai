''' Executing this module intitiates the application
    for emotion detection using Flask and deploys it
    on localhost:5000.
'''

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask('Emotion Detector')

@app.route('/emotionDetector')
def get_detector():
    ''' This function recieves text from the HTML interface
        and runs emotion detection on it using emotion_detector()
        function. The output shows the emotions and their scores,
        including the dominant emotion.
    '''

    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return 'Invalid text! Please try again!'

    formatted_response = "For the given statement, the system response is " \
                        f"'anger': {response['anger']}, 'disgust': {response['disgust']}, " \
                        f"'fear': {response['fear']}, 'joy': {response['joy']} " \
                        f"and 'sadness': {response['sadness']}. The dominant emotion " \
                        f"is {response['dominant_emotion']}."
    return formatted_response

@app.route('/')
def render_index():
    ''' This function renders the main application page
        using flask.
    '''
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
