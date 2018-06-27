class TempTracker(object):
    # Implement methods to track the max, min, mean, and mode
    temp = []
    t = 0
    mode = 0
    min = 0
    max = 0
    c = 0
    d = {}

    def insert(self, tmp):
        self.c = self.c + 1
        self.t = self.t + tmp
        if (len(self.d) == 0):
            self.min = tmp
            self.max = tmp
            self.mode = tmp
            self.d[tmp] = 1
        elif (tmp in self.d.keys()):
            if (self.min > tmp):
                self.min = tmp
            if (self.max < tmp):
                self.max = tmp
            self.d[tmp] = self.d[tmp] + 1
            if (self.d[tmp] > self.d[self.mode]):
                self.mode = tmp
        else:
            if (self.min > tmp):
                self.min = tmp
            if (self.max < tmp):
                self.max = tmp
            self.d[tmp] = 1

    def get_max(self):
        return self.max

    def get_min(self):
        return self.min

    def get_mean(self):
        return self.t / self.c

    def get_mode(self):
        return self.mode

tt=TempTracker()
tt.insert(10)
print(tt.get_max(),tt.get_min(),tt.get_mean(),tt.get_mode())
tt.insert(20)
print(tt.get_max(),tt.get_min(),tt.get_mean(),tt.get_mode())