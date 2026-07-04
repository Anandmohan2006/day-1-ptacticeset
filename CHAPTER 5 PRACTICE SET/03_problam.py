p1 = "buy now"
p2 = "click here"
p3 = "free trial"
p4 = "visit our website"     


message = input("Enter the message:")


if (p1 in message or p2 in message  or p3 in message or p4 in message):

    print("this message is a spam (dont click on it)")

else:
    print("this message is not a spam")