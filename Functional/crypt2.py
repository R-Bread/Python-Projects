let=['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
nsym=['1','2','3','4','5','6','7','8','9','0','@','#','_','&','-','+','(',')','/','*','\"',"\'",':',';','!','?']
text=input("Text:")
cypher=""

for a in text:
    if a in let:
        if len(let)==let.index(a)+1:
            cypher+=let[0]
        else:
            cypher+=let[let.index(a)+1]
    elif a.lower() in let:
        if len(let)==let.index(a.lower())+1:
            cypher+=let[0].upper()
        else:
            cypher+=let[let.index(a.lower())+1].upper()
    elif a in nsym:
        if len(nsym)==nsym.index(a)+1:
            cypher+=nsym[0]
        else:
            cypher+=nsym[nsym.index(a)+1]
    else:
        cypher+=a

print(cypher)    
#I am hungry, how 'bout you? "Wow!"
input("Press enter to exit.")

