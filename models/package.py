# from models.locations import Locations
# class Package:
#     package_id = 1
#     def __init__(self,start_location,end_location,weight,customer_name,customer_phone):
#         self._id = Package.package_id
#         Package.package_id += 1
#         self._start_location = Cities.city_validator(start_location)
#         self._end_location = Cities.city_validator(end_location)
#         if weight <= 0:
#             raise ValueError("Weight must be at least 1 kg.")
#         self._weight = weight
#         if not customer_name:
#             raise ValueError("Customer name cannot be empty.")
#         self._customer_name = customer_name
#         if not customer_phone.isdigit():
#             raise ValueError("Customer phone must contain only digits.")
#         self._customer_phone = customer_phone
#         self._status = PackageStatus.RECEIVED
        
#     @property
#     def id(self):
#         return self._id
    
#     @property
#     def start_loc(self):
#         return self._start_loc
    
#     @property
#     def end_loc(self):
#         return self._end_loc
    
#     @property
#     def status(self):
#         return self._status
    
#     def update_status(self):
#         if self.status == "Created":
#             self.status = "In Transit"
#         elif self.status == "In Transit":
#             self.status = "Delivered"

#     @staticmethod
#     def validate_phone(phone):
#         if not phone.isdigit():
#             raise ValueError("Phone number must contain only digits!")
#         if len(phone) != 10:  
#             raise ValueError("Phone number must be exactly 10 digits long!")
#         if not (phone.startswith("04") or phone.startswith(("02", "03", "07", "08"))):
#             raise ValueError("Phone number must start with 04 (mobile) or a valid area code (02, 03, 07, 08)!")
#         return phone
    
<<<<<<< HEAD
    @staticmethod
    def validate_weight(weight):
        if int(weight) <= 0:
            raise ValueError("The weight of a package can't be a negative number.")
        return weight
<<<<<<< HEAD
<<<<<<< HEAD
=======
    
    
>>>>>>> 9a4c026 (Created truck editted app_data, route,package)
=======
    
>>>>>>> 4c07a03 (Created CreateRoute)
=======
#     def __str__(self):
#         return (f"Package {self.id}: {self.start_location} to {self.end_location}\n"
#                 f"Weight: {self.weight}kg.\n"
#                 f"Customer: {self.customer_name} ({self.customer_phone})")
        


        
>>>>>>> 272ca14 (uasim's branch)
