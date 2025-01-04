from flask import Flask
from EmotionDetection.emotion_detection import emotion_detector

app = Flask('emotion detector app')

@app.route("/")
def emotionDetector():
    result_1 = emotion_detector('')   #'I think I am having fun'
    emotion_values_str = ", ".join(f"'{emotion}': {value}" for emotion, value in result_1.items() if emotion != "dominant_emotion") 
    formatted_output = f"For the given statement, the system response is {emotion_values_str}. The dominant emotion is {result_1['dominant_emotion']}."
    if result_1['dominant_emotion'] == None:
        return 'Invalid text! Please try again!.'
    return formatted_output
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)