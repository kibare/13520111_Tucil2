import matplotlib.pyplot as plt
from sklearn import datasets
from convexhull import myHull
import pandas as pd

x = True
while x:
    print("Berikut daftar dataset yang bisa digunakan: ")
    print("1. Iris")
    print("2. Breast Cancer")
    print("3. Wine")
    pilihan = int(input("Pilihan Dataset: "))
    
    if(pilihan >= 1 and pilihan<= 3):
        if(pilihan == 1):
            data = datasets.load_iris()
        elif(pilihan == 2):
            data = datasets.load_breast_cancer()
        elif(pilihan == 3):
            data = datasets.load_wine()
            
        df = pd.DataFrame(data.data, columns=data.feature_names) 
        df['Target'] = pd.DataFrame(data.target)
        jumlahAttribut = len(data.feature_names)
        
        print(" ")
        print("Berikut daftar attribute: ")
        for i in range(jumlahAttribut):
            print(str(i+1) + "." +data.feature_names[i])
        x = int(input("Pilihan attribute x: "))
        y = int(input("Pilihan attribute y: "))
        
        if ((x>=1 and x<= jumlahAttribut) and (y>=1 and y <= jumlahAttribut) and (x != y)):
            plt.figure(figsize = (10, 6))
            label = len(df['Target'].unique())
            colors = ['b','r','g']

            plt.title(str(data.feature_names[x-1])+" vs "+str(data.feature_names[y-1]))
            plt.xlabel(data.feature_names[x-1])
            plt.ylabel(data.feature_names[y-1])

            for i in range(label):
                bucket = df[df['Target'] == i]
                bucket = bucket.iloc[:,[x-1,y-1]].values
                hull = myHull(bucket)   #implementasi convexhull
                plt.scatter(bucket[:, 0], bucket[:, 1], label=data.target_names[i], color=colors[i])
                for simplex in hull:
                    plt.plot(bucket[simplex, 0], bucket[simplex, 1], color=colors[i])
            plt.legend()
            plt.show()
            plt.close('all')
        else:
            print("invalid attribute")
    else:
        print("Masukan Salah")
        
    endState = input("\nMau coba dataset yang lain? (Y/N): ")
    if endState.upper() != "Y":
        x = False
        

