import openai
import speech_recognition as sr
from gtts import gTTS
import os

# OpenAI API key
openai.api_key = "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"

def listen_and_respond():
    """
    Listen for audio input, recognize it and respond using OpenAI
    """
    # Create speech recognizer object
    r = sr.Recognizer()

    # Listen for input
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    # Try to recognize the audio in Turkish
    try:
        prompt = r.recognize_google(audio, language="tr-TR")
        print("You asked:", prompt)

        # Use OpenAI to create a response
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            temperature=0.7,
            max_tokens=300,
            stop=None  # Optional: If you have a specific stopping condition, you can use it here.
        )

        # Get the response text
        response_text = str(response['choices'][0]['text']).strip('\n\n')
        print(response_text)

        # Speak the response in Turkish using gTTS
        tts = gTTS(text=response_text, lang="tr")
        tts.save("response.mp3")
        os.system("start response.mp3")  # This will play the audio using the default audio player

    # Catch if recognition fails
    except sr.UnknownValueError:
        response_text = "Sorry, I didn't understand what you said"
        print(response_text)
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

def main():
    while True:
        listen_and_respond()

if __name__ == "__main__":
    main()
