
from microsoftcognitive import MicrosoftVision


import pprint

mv = MicrosoftVision('f30f769d21a446fb98f0b12909841f6a',MicrosoftVision.VisualService.ANALYZE)
mv.setParameters({mv.VisualFeature.CATEGORIES})
result  = mv.jsonRecognizeImageFromFile('https://oxfordportal.blob.core.windows.net/vision/Analysis/3.jpg')

print result

