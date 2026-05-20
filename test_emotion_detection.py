import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        res_joy = emotion_detector("I am glad this happened")
        self.assertEqual(res_joy['dominant_emotion'], 'joy')
        
        res_anger = emotion_detector("I am really mad about this")
        self.assertEqual(res_anger['dominant_emotion'], 'anger')
        
        res_disgust = emotion_detector("I am disgusted just hearing about this")
        self.assertEqual(res_disgust['dominant_emotion'], 'disgust')
        
        res_sadness = emotion_detector("I am so sad about this")
        self.assertEqual(res_sadness['dominant_emotion'], 'sadness')
        
        res_fear = emotion_detector("I am really afraid of this happening")
        self.assertEqual(res_fear['dominant_emotion'], 'fear')

if __name__ == '__main__':
    unittest.main()