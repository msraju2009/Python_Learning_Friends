class Battery:
    def __init__(self, size=85):
        self.size = size
        self.charge_level = 0

    def get_range(self):
        if self.size == 85:
            print("Battery Distance range is 260 kms ")
        elif self.size == 100:
            print("Battery Distance range is 310 kms ")
