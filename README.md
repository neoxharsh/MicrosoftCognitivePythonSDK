# MicrosoftCognitivePythonSDK
Python Wrapper around Microsoft Cognitive API

This is the first Beta version of python wrapper for Microsoft Cognitive API.

The original SDK example is complicated and needs a good wraper. So I made a nice easy to use wrapper around the main code, making it more friendly for beginners. 
It is still in beta phase so, expect bugs and Exception. 

It uses simple python "request" module to do API post request. JSON data can be gathered in just four line of codes.


Modify the code, contribute to the development and share to make it popular. 

To make a simple request, first import "microsoftVision"from "microsoftcognitive"

```python
from microsoftcognitive import MicrosoftVision
```

Then create a MicrosoftVision object by passing the API key as the first argument and the Microsoft Vision Service to be used. Constants are provied to add the service easily. 

API can be obtained by going to https://portal.azure.com
Signup for an account and than on the dashboard, click the "+" sign on the left bar, select Intelligence, and create a new Cognitive Service Account, select the API type to Computer Vision. Once the Service is created, you will be able to get the API key from the top right corner of the computer vision dashboard, click the key icon. select anyone of the two keys, and keep it private, cause the free account only gives you a limited number of API calls. 

```python
mv = MicrosoftVision('[Insert API Key]',MicrosoftVision.VisualService.ANALYZE)
```

Then set the visual features that need to be extracted as described by Microsoft. Constants are also provided for the same. Multiple features can be added, by passing them in curly braces and seperating with comma. { , }

```python
mv.setParameters({mv.VisualFeature.CATEGORIES})
```

Now get the json object returned by the Cognitive API by passing the image file or URL of the image to jsonRecognizeImageFromFile() or jsonRecognizeImagefromURL() respectively.

```python
# for URL
result  = mv.jsonRecognizeImageFromURL('https://oxfordportal.blob.core.windows.net/vision/Analysis/3.jpg')

# for File
result  = mv.jsonRecognizeImageFromFile('file')
```
The complete code will look like this

```python
from microsoftcognitive import MicrosoftVision

mv = MicrosoftVision('[Insert API Key]',MicrosoftVision.VisualService.ANALYZE)
mv.setParameters({mv.VisualFeature.CATEGORIES})
result  = mv.jsonRecognizeImageFromURL('https://oxfordportal.blob.core.windows.net/vision/Analysis/3.jpg')

print result
```

An example app is also give, just enter the API key provided from Azure Console. 
