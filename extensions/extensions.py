media = input("what is your file name " ).strip().lower()

if ".jpg" in media:
    print("image/jpeg")
elif ".pdf" in media:
    print("application/pdf")
elif ".gif" in media:
    print ("image/gif")
elif ".jpeg" in media:
    print("image/jpeg")
elif ".png" in media:
    print("image/png")
elif ".txt" in media:
    print("text/plain")
elif ".zip" in media:
    print("application/zip")

else:
    print("application/octet-stream")