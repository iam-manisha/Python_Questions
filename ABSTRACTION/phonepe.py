from abc import ABC, abstractmethod


class Payment(ABC):

    @abstractmethod
    def pay(self):
        pass


class PhonePe(Payment):

    def pay(self):
        print("Payment done using PhonePe")


class GooglePay(Payment):

    def pay(self):
        print("Payment done using Google Pay")


p1 = PhonePe()
p1.pay()

p2 = GooglePay()
p2.pay()
