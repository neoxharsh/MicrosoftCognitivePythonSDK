
from microsoftcognitive import MicrosoftVision


import pprint

mv = MicrosoftVision('',MicrosoftVision.VisualService.ANALYZE)
mv.setParameters({mv.VisualFeature.CATEGORIES})
result  = mv.jsonRecognizeImageFromURL('https://oxfordportal.blob.core.windows.net/vision/Analysis/3.jpg')

print result

