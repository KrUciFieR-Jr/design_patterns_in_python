"""
In Factory we would have superclass define the object creation using interfaces
and subclass would be handling the actual implementation

Key Principles:
- decoupling -> client doesn't need know how the notification is getting created and how it is going to send
it only needs to know what type of notification a creator will produce and what functions does the notifications have

- Extensibility
-> in this we can create a slack notification factory which does slack notifications, by maintaining the contract, all it client needs to know
the right input and we handle the execution


In real world scenarios:
This is used when we don't know what to create until runtime, since the input will be dynamic in nature
For in GUI framework, there would a WindowsButton, MacButton for an application

Factory method will create the button based on the host operating system

Benefits

- Flexibility
- Code resubaility


Drawbacks

- Increased complexity
- Big codebase to handle
"""
from abc import ABC, abstractmethod

class Notification(ABC):
    """Notification is my product, there would be different kinds of notifcation
    but notification is supposed to just notify
    """
    @abstractmethod
    def notify(self, message):
        pass

# Now these are the different notifications types

# Concrete Products
class EmailNotification(Notification):
    def notify(self, message: str):
        return f"Sending email with message: {message}"

class SMSNotification(Notification):
    def notify(self, message: str):
        return f"Sending SMS with message: {message}"

class PushNotification(Notification):
    def notify(self, message: str):
        return f"Sending push notification with message: {message}"
    

class NotificationFactory(ABC):
    """ This is my product creator interface, which is responsible for defining
    What kind of functions does a Product creator need to have
    In this case, my factory will create a product 
    so NotificationFactory creates Notification
    """
    @abstractmethod
    def create_notification(self)-> Notification:
        pass


# Concrete Factories
class EmailNotificationFactory(NotificationFactory):
    def create_notification(self) -> Notification:
        return EmailNotification()

class SMSNotificationFactory(NotificationFactory):
    def create_notification(self) -> Notification:
        return SMSNotification()

class PushNotificationFactory(NotificationFactory):
    def create_notification(self) -> Notification:
        return PushNotification()
    


# client will use it like this

def send_notification(factory: NotificationFactory, message:str):
    """In this client doesn't need to how the notification will be notify
    It knows factory create a type of notification, and its job is to notify
    thereby decoupling
    """
    notification = factory.create_notification()
    print(notification.notify(message))

if __name__ == "__main__":
    send_notification(EmailNotificationFactory(), "Welcome to our service!")
    send_notification(SMSNotificationFactory(), "Your code is 1234")
    send_notification(PushNotificationFactory(), "You have a new message")


"""
    Sometimes, factories may need to create products based on input parameters. 
    For example, instead of creating separate factories for each product, you might have a single factory that takes an argument and returns the appropriate product.

    class NotificationFactory:
    def create_notification(self, notification_type: str) -> Notification:
        if notification_type == "email":
            return EmailNotification()
        elif notification_type == "sms":
            return SMSNotification()
        elif notification_type == "push":
            return PushNotification()
        else:
            raise ValueError(f"Unknown notification type: {notification_type}")

# Usage
factory = NotificationFactory()
notification = factory.create_notification("email")
print(notification.notify("This is an email notification"))
    """