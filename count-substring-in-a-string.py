def count_substring(string, sub_string):
    count = 0
    for i in range(0,len(string)):
        substr = string[i:i+len(sub_string)]
        
        if len(substr) == len(sub_string):
            #print i, substr
            if substr == sub_string:
                #print i, substr
                count += 1
     
    return count
       
        
 if __name__ == '__main__':
    string = raw_input().strip()
    sub_string = raw_input().strip()
    
    count = count_substring(string, sub_string)
    print count
