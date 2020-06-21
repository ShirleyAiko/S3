class SMS_store:
    
    def __init__(self):
        self.from_number = []
        self.time_arrived = []
        self.text_of_SMS = []
        self.has_been_viewd = []
        
    def add_new_arrival(self, number, time, text):
        self.from_number.append(number)
        self.time_arrived.append(time)
        self.text_of_SMS.append(text)
        self.has_been_viewd.append(False)
        
    def ChangeCondition(self, i):
        self.has_been_viewd[i] = True
    
    def message_count(self):
        return len(self.from_number)
        
    def get_unread_indexes(self):
        s = 0
        for i in range(len(self.has_been_viewd)):
            if self.has_been_viewd[i] == False:
                s += 1
        return s
    
    def get_message(self, i):
        for i in range(len(self.from_number)):
            if self.from_number[i] != "":
                self.has_been_viewd.ChangeCondition(i)
                return self.from_number[i], self.time_arrived[i], self.text_of_SMS[i]
            else:
                return None
            
    def delete(self, i):
        self.text_of_SMS[i] = ""
    
    def clear(self):
        self.from_number = []
        self.time_arrived = []
        self.text_of_SMS = []