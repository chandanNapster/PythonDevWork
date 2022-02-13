class Complex:

    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def add(self, number):
        real = self.real + number.real
        imag = self.imag + number.imag
        result = Complex(real, imag)
        return result

    def __str__(self):
        return ("The real part is ::" + str(self.real) + "\n"+"The imaginery part is ::" + str(self.imag))
