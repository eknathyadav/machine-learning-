##k means clustering
d=input("Enter dataset elements  : ")
data_set = d.split()
print(data_set)
mean1=input("Enter mean 1")
mean2=input("Enter mean 2")
def makingclusters(m1,m2,dataset_):
    cluster1=[]
    cluster2=[]
    for i in dataset_:
        a=int(m1)-int(i)
        b=int(m2)-int(i)
        if abs(a)<abs(b):##to convert negative number to positive
            cluster1.append(i)
        else:
            cluster2.append(i)
    return (cluster1,cluster2)
def calnewmean(c1,c2):
    sum_mean1=0
    sum_mean2=0
    for i in c1:
        sum_mean1=sum_mean1+int(i)
    for j in c2:
        sum_mean2=sum_mean2+int(j)
    new_m1=sum_mean1/len(c1)
    new_m2=sum_mean2/len(c2)
    return (new_m1,new_m2)
old_mean1=mean1
old_mean2=mean2
clust1,clust2=makingclusters(mean1,mean2,data_set)##To return 2 values from function##unpack tuples
n_mean1,n_mean2=calnewmean(clust1,clust2)
mean1=n_mean1
mean2=n_mean2
count=0
while(old_mean1!=mean1 and old_mean2!=mean2):
    count+=1
    clust1,clust2=makingclusters(mean1,mean2,data_set)
    print("After Iteration"+str(count)+":")
    print(clust1)
    print(clust2)
    old_mean1=mean1
    old_mean2=mean2
    n_mean1,n_mean2=calnewmean(clust1,clust2)
    mean1=n_mean1
    mean2=n_mean2
    print("New mean 1 : " +str(mean1))
    print("New mean 1 : " +str(mean2))
    print("--------------------------------------------------------------------------------------")



    
    
    













        






