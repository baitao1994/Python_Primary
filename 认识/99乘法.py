for i in range(1,10):
    for j in range(1,i+1):
        print("{}*{}={}".format(i,j,i*j),end=" ")  #不加end=" "这句，print就直接换了行
    print("\n")
  
