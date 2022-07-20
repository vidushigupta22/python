
 
# title : Title of the notification.
# message : Message of the notification.
# app_name : Name of the app launching this notification.
# app_icon : Icon to be displayed along with the message.
# timeout : time to display the message for, defaults to 10.


import time
from plyer import notification


if __name__== '__main__':
   
    notification.notify(
        title = 'Drink your H20 NOW',
        message = '''The U.S. National Academies of Sciences, Engineering, and Medicine determined that an adequate daily fluid intake is:
        About 15.5 cups (3.7 liters) of fluids a day for men
        About 11.5 cups (2.7 liters) of fluids a day for women''',
        app_name = 'Water reminder',
        # app_icon = 'C:\\Users\\user\\Documents\\python\\Projects\\drink.ico',
        timeout = 10 )
# time.sleep(10)