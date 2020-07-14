class Vehicle:
    '''
    Vehicle class
    '''

    def __init__(self, brand, type, model):
        self.brand = brand
        self.model = model
        self.type = type
        self.gas_tank_size = 35
        self.fuel_level = 0

    def fuel_up(self):
        print("Initial fuel level is {} ".format(self.fuel_level))
        self.fuel_level = self.gas_tank_size
        print("After fuelUP, fuel level is {} ".format(self.fuel_level))

    def drive(self):
        print("The {} is now driving ".format(self.model))

    # creating a method to update an attribute's value , after class introduction
    def update_fuel_level(self, new_level):
        if new_level <= self.gas_tank_size:
            self.fuel_level = new_level
            print(self.fuel_level)
        else:
            print("Exceeded fuel tank capacity ")


# Constructing an object
vehicle_obj = Vehicle('Maruti', 'HatchBack', 'Celerio')
Vehicle.drive(vehicle_obj)  # usage of self

# Calling methods
vehicle_obj.drive()
# updating the fuel tank
vehicle_obj.fuel_up()
# Accessing attribute values
print(vehicle_obj.fuel_level)
print(vehicle_obj.brand)
print(vehicle_obj.model)
print(vehicle_obj.type)
# Creating multiple objects
honda = Vehicle('Honda', 'CRV', 'SUV')
vw = Vehicle('VW', 'Passat', 'Sedan')
hyundai = Vehicle('Hyundai', 'i20', 'Hatchback')
honda.drive()
# Modifying an attribute directly
hyundai.fuel_level = 50
print(hyundai.fuel_level)
vw.drive()
hyundai.drive()
vw.update_fuel_level(20)


class ElectricVehicle(Vehicle):
    def __init__(self, brand, model, type):
        # calling super class contructor with class name
        Vehicle.__init__(self, brand, model, type)
        # calling super class contructor with super() function
        # super().__init__(brand, model, type)
        self.battery_size = 85
        self.charge_level = 0
        from Battery import Battery
        # Storing an instance of a class in an attribute
        self.battery = Battery()

    # Adding new methods to a child class
    def charge(self):
        self.charge_level = 100
        print("Vehicle is fully charged now")

    # Overriding parent methods
    def fuel_up(self):
        print("The vehicle has no fuel tank ")


electric_vehicle = ElectricVehicle(brand='Tesla', model='Model 3', type='Car')
electric_vehicle.charge()
electric_vehicle.drive()
# Using The Instance of battery and calling its functions
electric_vehicle.battery.get_range()


# class variables example

class CSEStudents:
    branch = 'CSE'  # branch value is shared across all instances of CSEStudents

    def __init__(self, name, roll_no):
        self.student_name = name  # instance variables differ from different instances
        self.student_roll_no = roll_no


kalyan = CSEStudents('Kalyan', 92910)
print(kalyan.student_name)
print(kalyan.student_roll_no)
print(kalyan.branch)

sai = CSEStudents('SAI', 20010100)
print(sai.student_name)
print(sai.branch)


# Single Inheritance/ Simple inheritance

class Parent:
    def show(self):
        print("Hello from Parent")


class Child(Parent):
    def display(self):
        print("From Child class")


c_obj = Child()
c_obj.show()
c_obj.display()


# Multilevel inheritance
class A:
    def method_a(self):
        print("From Class A")


class B(A):
    def method_b(self):
        print("From class B")


class C(B):
    def method_c(self):
        print("From Class C")


c_obj = C()
c_obj.method_a()
c_obj.method_b()
c_obj.method_c()


# Multiple inheritance
class A:
    def method_a(self):
        print("From Class A")


class B:
    def method_b(self):
        print("From class B")


class C:
    def method_c(self):
        print("From Class C")


class D(A, B, C):
    def method_d(self):
        print("From class D")


d_obj = D()
d_obj.method_a()
d_obj.method_b()
d_obj.method_c()
d_obj.method_d()


# Hierarchial inheritance
class A:
    def method_a(self):
        print("From Class A")


class B(A):
    def method_b(self):
        print("From class B")


class C(A):
    def method_c(self):
        print("From Class C")


b = B()
b.method_a()
b.method_b()
c = C()
c.method_a()
c.method_c()


# Example of MRO (Method Resolution Order)
class Agile:
    def create(self):
        print("From Agile class")


class Dev(Agile):
    def create(self):
        print("From Dev class")


class QA(Agile):
    def create(self):
        print("From QA class")


class Sprint(Dev, QA):
    pass


sprint = Sprint()
# sprint.create()
print(Sprint.__mro__)
