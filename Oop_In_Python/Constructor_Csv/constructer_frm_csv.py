#constructor_frm_csv_file
import csv
class ITEM:
    all=[]
    def __init__(self,Make,ID,Year):
        self.Make=Make
        self.ID=ID
        self.Year=Year
        ITEM.all.append(self)
        #getting instants from csv
    @classmethod
    def inst_csv(cls):
        with open ("cars.csv","r")as f:
         reader=csv.DictReader(f)
         items=list(reader)
        for i in items:
            ITEM (
                Make = i.get('Make'),
                ID=i.get('ID'),
                Year=i.get('Year'),
            )
    def __repr__(self):
        return f"ITEM('{self.Make}','{self.ID}','{self.Year})"
    




ITEM.inst_csv()
print(ITEM.all)