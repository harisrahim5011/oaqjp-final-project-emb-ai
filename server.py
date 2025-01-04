'''import module from flask
'''
from flask import Flask,render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask('emotion detector app')


@app.route("/")
def render_index_page():
    '''render the index page
    '''
    return render_template('index.html')

@app.route("/emotionDetector")
def emot_detector():
    '''get the json formatted result, exclude 'dominant' and show seperately 
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    result_1 = emotion_detector(text_to_analyze)   # I think I am having fun
    emotion_values_str = ", ".join(f"'{emotion}': {value}"
                                   for emotion, value in result_1.items()
                                   if emotion != "dominant_emotion"
                                    )
    formatted_output = (f"For the given statement, the system response is "
                        f"{emotion_values_str}. "
                        f"The dominant emotion is {result_1['dominant_emotion']}."
                        )
    if result_1['dominant_emotion'] is None:
        return 'Invalid text! Please try again!.'

    return formatted_output

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
