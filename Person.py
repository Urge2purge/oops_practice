class Person:
    def __init__(self, loan_id, month, loan_status):
        self.loan_id = loan_id
        self.month = month
        self.loan_status = loan_status

    def display(self):
        print(self.loan_id,",",self.month,",",self.loan_status)

    def talk():
        pass

if __name__ == "__main__":
    p1 = Person("001","20240131","3")
    p1.display()
    p1.talk()
    