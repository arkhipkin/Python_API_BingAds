# Python API for BingAds usage
I am sharing with you that small project because Documentation of Bing Ads API is a bit confusing.
Main links:
- [Get Started Using Python with Bing Ads Services](https://docs.microsoft.com/en-us/bingads/guides/get-started-python?view=bingads-12)
- [Bing Ads Client Libraries](https://docs.microsoft.com/en-us/bingads/guides/client-libraries?view=bingads-12)
- [BingAds-Python-SDK on GitHub](https://github.com/BingAds/BingAds-Python-SDK)
- [Walkthrough: Bing Ads Desktop Application in Python](https://docs.microsoft.com/en-us/bingads/guides/walkthrough-desktop-application-python?view=bingads-12)

## Preparations
### [Get a Developer Token](https://docs.microsoft.com/en-us/bingads/guides/get-started?view=bingads-12#get-developer-token)
Generated secret API Access Key for your Marketing BingAds account.

### [Register Your Application](https://docs.microsoft.com/en-us/bingads/guides/authentication-oauth?view=bingads-12#registerapplication)
Before you can manage authentication for users of your Bing Ads application, you must register your application and get the corresponding client ID and client secret. Go to https://apps.dev.microsoft.com/ for that goal.

After Application creation and saving of all your changes - take note of your **Application Id**. You will use it as the CLIENT_ID in the OAuth grant flow.

Also take note of your Password and redirect URI if you registered a web application. The passsword will be used as the CLIENT_SECRET in the OAuth grant flow.

For introductory code samples, technical guides, and reference content, see the [Bing Ads API Documentation](https://docs.microsoft.com/en-us/bingads/).

