import csv
import pandas as pd


class Hashtable():
    def __init__(self) -> None:
        self.MAX = 100
        self.arr = [[] for i in range(self.MAX)]
    
    def get_hash(self, key):
        hash = 0
        for char in key:
            #Gets the assci value for each character
            hash += ord(char)
        return hash % self.MAX
    
    def __setitem__(self, key, value):
        h = self.get_hash(key)
        #self.arr[h] = value
        found = False

        for idx, element in enumerate(self.arr[h]):
            print(self.arr[h])
            print(idx, element)
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key, value)
                found = True
                break
        if not found:
            self.arr[h].append((key, value))

    def __getitem__(self, key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]
        #return self.arr[h]
    
    def __delitem__(self, key):
        h = self.get_hash(key)
        for index, element in enumerate(self.arr[h]):
            if element[0] == key:
                 del self.arr[h][index]
        del self.arr[h]

    
    def avg():
        #Read the csv file
        df = pd.read_csv('nyc_weather.csv')
        #iloc lets you start from the second row in the second column  
        sc = df.iloc[1:,1]
        #has a built in function to calculate the smean
        mean = sc.mean()
        print(f"AVERAGE: {mean}")


    def max():
        #Read the csv file
        df = pd.read_csv('nyc_weather.csv')
        #iloc lets you start from the second row in the second column  
        sc = df.iloc[1:,1]
        #has abuilt in function to calculate the smean
        max = sc.max()
        print(f"MAX: {max}")


    def find_temp(self, date):
        df = pd.read_csv('nyc_weather.csv')
        cvs_date = df[['date','temperature(F)']]
        #print(cvs_date)
        for index, row in cvs_date.iterrows():
             if row['date'] == date:
                 #print(row['date'] , row['temperature(F)'])
                 return row['temperature(F)']
        return "Date not found"


    # def per_word(self):
    #     wrd_cnt = {}
    #     with open("poem.txt", "r")as f:
    #         #wrd = f.read().split(' ')
    #         #print(wrd)
    #         for token in f:
    #             #print(token)
    #             for j in token.split():
    #             #token=token.replace('\n','')
    #                 print(j)
    #             #if wrd in token.split():
    #                 wrd_cnt[token]+=1
    #             #else:
    #                 wrd_cnt[token]=1
    #         return wrd_cnt
    #     #     for word in wrd:
    #     #         wrd_cnt.extend(word.split())
    #     # return wrd_cnt
                
                

        # df = pd.read_csv("poem.txt")
        # txt_wrd = dff

        # for i, j in df.iterrows():
        #     print(i, j)
    def hey(self):
        wrd_cnt = {}
        with open('poem.txt', 'r') as file:
            lines = file.read().splitlines()  # Read and split lines
            
        cnt = 0

        # Create a DataFrame with each line as a row
        df = pd.DataFrame(lines)
        print(df)
        for i in df:
            print(type(i))
            i_str = str(i.split())
            print(i_str)
            for j in i_str:
                cnt += 1
                print(j)
                print('\n')
                if i in wrd_cnt:
                    cnt += 1
                    wrd_cnt[i] += 1
                else:
                    wrd_cnt[i] = 1
        return cnt


    def hey_hey(self):
        with open('poem.txt', 'r') as file:
            text = file.read()
            
            
        lines = text.split('\n')
        print(lines)

# Step 3: Define column names
        columns = ['Word']

# Step 4: Create the DataFrame with the specified columns
        #df = pd.DataFrame({'Line Number': range(1, len(lines) + 1), 'Text': lines})
        df = pd.DataFrame(lines, columns=columns)

# Display the DataFrame
        print(df)


        # Display the DataFrame
        #print(df)



    # def hey_no(self):
    #     word_count = {}
    #     with open("poem.txt","r") as f:
    #         for line in f:
    #             tokens = line.split(' ')
    #             for token in tokens:
    #                 token=token.replace('\n','')
    #                 if token in word_count:
    #                     word_count[token]+=1
    #                 else:
    #                     word_count[token]=1



    avg()
    max()
    #find_temp("jan 7")

if __name__ == '__main__':
    hh = Hashtable()
    hh["march 7"] = 123
    hh["march 8"] = 220
    #print(hh.arr)
    #print(hh["march 7"])
    print(hh.find_temp("Jan 7"))
    print(hh.find_temp("Jan 4"))
    print(hh.find_temp("Jan 9"))
    #hh.per_word
    #print(hh.hey())
    #print(hh.hey_no)


