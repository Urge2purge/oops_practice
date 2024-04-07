class Person:
    def __init__(self, loan_id, month, loan_status, ltv, fico):
        self.loan_id = loan_id
        self.month = month
        self.loan_status = loan_status
        self.ltv = ltv
        self.fico = fico

    def display(self):
        print(self.loan_id,",",self.month,",",self.loan_status)

    def loan_char(self):
        print("Loan-to-Value ratio is",self.ltv)
        print("FICO score is", self.fico)

if __name__ == "__main__":
    p1 = Person("044","20240131","C", 90, 833)
    p1.display()
    p1.loan_char()
    