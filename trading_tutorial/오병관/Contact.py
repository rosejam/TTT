class Contact:
    def __init__ (self, name, phone_number, e_mail, addr):
        self.name = name
        self.phone_number=phone_number
        self.e_mail = e_mail
        self.addr = addr
    def __init__(self):
        pass
    def print_info(self):
        print("Name: ", self.name)
        print("Phone Number: ",self.phone_number)
        print("E-mail: ",self.e_mail)
        print("Address: ",self.addr)

def run():
    kim=Contact("김일구", "010-8812-1193", "ilgu.kim@python.com", "Seoul")
    kim.print_info()

if __name__=="__main__":
    run()