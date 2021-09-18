import time


class Sleep:

    @staticmethod
    def sleep_two_sec(self):
        time.sleep(2)
        print("Погодите пару секунд...")

    @staticmethod
    def sleep_three_sec(self):
        time.sleep(3)
        print("Погодите три секунды...")
