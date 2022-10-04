import instaloader

ig= instaloader.Instaloader()
dp=input("enter insta user name:")

ig.download_profile(dp,profile_pic_only=True)
