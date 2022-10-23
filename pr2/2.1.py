def main():
    a=input()
    s3=[]
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if a[i]==a[j]:
                s3.append(a[i:j])
                break
        else:
            s3.append(a[i:j+1])
    print(max(s3, key=len))
if __name__=="__main__":
    main()