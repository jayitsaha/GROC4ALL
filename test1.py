# s = "i want twenty five eggs"
# list = {"twenty":"1" , "thirty":"1" , "fourty":"1" , "fifty":"1","sixty":"1","seventy":"1","eighty":"1","ninety":"1"}

s = "i want fifty five eggs"


dict_trivial = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8","nine":"9", "ten":"10"}
dict_teen = {"eleven":"11", "twelve":"12", "thirteen":"13", "fourteen":"14", "fifteen":"15","sixteen":"16", "seventeen":"17", "eighteen":"18", "nineteen":"19"}

dict_large = {"twenty one":"21", "twenty two":"22", "twenty three":"23", "twenty four":"24", "twenty five":"25", "twenty six":"26","twenty seven":"27", "twenty eight":"28", "twenty nine":"29","twenty":"20",
"thirty one":"31", "thirty two":"32", "thirty three":"33", "thirty four":"34", "thirty five":"35", "thirty six":"36","thirty seven":"37", "thirty eight":"38", "thirty nine":"39","thirty":"30",
"fourty one":"41", "fourty two":"42", "fourty three":"43", "fourty four":"44", "fourty five":"45", "fourty six":"46","fourty seven":"47", "fourty eight":"48", "fourty nine":"49","fourty":"40",
"fifty one":"51", "fifty two":"52", "fifty three":"53", "fifty four":"54", "fifty five":"55", "fifty six":"56","fifty seven":"57", "fifty eight":"58", "fifty nine":"59","fifty":"50",
"sixty one":"61", "sixty two":"62", "sixty three":"63", "sixty four":"64", "sixty five":"65", "sixty six":"66","sixty seven":"67", "sixty eight":"68", "sixty nine":"69","sixty":"60",
"seventy one":"71", "seventy two":"72", "seventy three":"73", "seventy four":"74", "seventy five":"75", "seventy six":"76","seventy seven":"77", "seventy eight":"78", "seventy nine":"79","seventy":"70",
"eighty one":"81", "eighty two":"82", "eighty three":"83", "eighty four":"84", "eighty five":"85", "eighty six":"86","eighty seven":"87", "eighty eight":"88", "eighty nine":"89","eighty":"80",
"ninety one":"91", "ninety two":"92", "ninety three":"93", "ninety four":"94", "ninety five":"95", "ninety six":"96","ninety seven":"97", "ninety eight":"98", "ninety nine":"99","ninety":"90",
}

list = {"twenty":"1" , "thirty":"1" , "fourty":"1" , "fifty":"1","sixty":"1","seventy":"1","eighty":"1","ninety":"1"}
flag = 0
for i in list:
    print(i)
    x = s.find(i)
    print(x)
    if(s.find(i)>=0):
        print(i)
        for k in dict_large:
            if(s.find(k)):
                s = s.replace(k,dict_large[k])
                flag = 1

print("FLAg")

print(flag)
flag1 = 0
if(flag==0):
        # print("HIII")
    for j in dict_teen:
        if(s.find(j)>=0):
            s = s.replace(j,dict_teen[j])
            print(j)

            flag1 = 1
print("FLAG 1")
print(flag1)
if(flag1==0):
        # print("HIII")
    for x in dict_trivial:
        if(s.find(x)):
            s = s.replace(x,dict_trivial[x])



print(s)