class PalindromeLogic:

    def string_palindrome(self, st):
        out = ""
        for i in st:
            out = i + out
        if st == out:
            return True
        else:
            return False

    def number_palindrome(self, n):
        dup = n
        out = 0
        while dup != 0:
            rem = dup % 10
            out = out * 10 + rem
            dup //= 10
        if n == out:
            return True
        else:
            return False


class User(PalindromeLogic):
    def __init__(self, num):
        self.num = num

    def result(self):
        if type(self.num) == str:
            if self.string_palindrome(self.num):
                print("Its a Palindrome")
            else:
                print("Not a Palindrome")
        elif type(self.num) == int:
            if self.number_palindrome(self.num):
                print("Its a Palidrome")
            else:
                print("Not a Palidrome")
        else:
            print("Implementation in Process")


u1 = User([10, 20, 30])
u1.result()
