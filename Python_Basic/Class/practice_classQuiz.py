class House:
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year


    def show_detail(self):
        
        print("{0} {1} {2} {3} {4} ".format(self.location, self.house_type, self.deal_type, self.price, self.completion_year))

gangnam = House("강남", "아파트", "매매", "10억", "2010년")
mapo = House("마포", "오피스텔", "전세", "5억", "2007년")
songpa = House("송파", "빌라" , "월세", "500/50", "2000년")

list = []
list.append(gangnam)
list.append(mapo)
list.append(songpa)

print("총 " + str(len(list)) + "대의 매물이 있습니다.")
print("총 {0}대의 매물이 있습니다.".format(len(list)))
for sale in list : 
    sale.show_detail()