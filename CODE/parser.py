
def reduce(stack,pro_matrix):
 for i in range(len(pro_matrix)):
      for j in range(len(pro_matrix[i])):
           x=pro_matrix[i][len(pro_matrix[i])-j-1];
           result=stack.endswith(x);
           if(result==True):
            stack=stack.replace(x,pro_matrix[i][0]);
            #print('I am inside reduce'+stack+' x is '+x);
            return stack;
 return 'ERROR'; 

def findx(stack,op_list):
     s=0;
     x='$';
     for i in range(len(stack)):
          for j in range(len(op_list)):
           if (stack[len(stack)-i-1]==op_list[j] and s!=1):
               x=stack[len(stack)-i-1];
               #print(op_list[j]+'x is'+x);
               return x;
     return '$';     
               
#taking production rules:
#taking precendence file as input
f1=open('grammar.txt','r');
pro_list=f1.readlines();
f1.close();
for i in range (len(pro_list)):
    pro_list[i]=pro_list[i].strip('\n');
i=0;
#for taking out all the empty spaces created by the above loop
while(i<len(pro_list)):        
    if (not pro_list[i]):
        pro_list.pop(i)
        i=0
    i+=1      
pro_list.sort(key = len)
print('hii')
print(pro_list);

i=0;
pro_matrix=[];
for i in range(len(pro_list)):
     temp_list=[];
     temp_str=pro_list[i];
     j=0;
     index=temp_str.index('->');
     #print(index);
     LHS=temp_str[:index];
     temp_list.append(LHS);
     RHS=temp_str[index+2:];
     #print(LHS);
     #print(RHS);
     list=RHS.split('|');
     temp_list+=list;
     pro_matrix.append(temp_list);
     #print(temp_list);

i=0;
j=0;
for i in range(len(pro_matrix)):
     for j in range(len(pro_matrix[i])):
          pro_matrix[i].sort(key = len)
          print(pro_matrix[i][j],end =" ")
     print("");     

     
#---------------------------------------------------------------------------------------------------------------------------------------

          

     



#-------------------------------------------------------------------------------------
#taking precendence file as input
f=open('precedence.txt','r');
list1=f.readlines();
f.close();
for i in range (len(list1)):
    list1[i]=list1[i].strip('\n');
    list1[i]=list1[i].strip(' ');
i=0;

#for taking out all the empty spaces created by the above loop
while(i<len(list1)):        
    if (not list1[i]):
        list1.pop(i)
        i=0
    i+=1      
#print(list1);


#creating lists
op_list=[];
order_list=[];
lr_list=[];

# appending $
op_list.append('i');
order_list.append(-1);
lr_list.append('@');

j=0;
for i in range (len(list1)):
     m1=len(list1[i]);
     str1=list1[i];
     k=0;
     
     for k in range(m1):
          
          if(str1[k]!=' ' and str1[k]!='l' and str1[k]!='r'):
           #print(str1[k]);
           op_list.append(str1[k]);
           order_list.append(i+1);
           lr_list.append(str1[m1-1]);

# appending id
op_list.append('(');
order_list.append(99);
lr_list.append('r');
op_list.append(')');
order_list.append(0);
lr_list.append('l');
op_list.append('$');
order_list.append(100);
lr_list.append('@');
           
#print(op_list);
#print(order_list);
#print(lr_list);

#creating table
i=0;
j=0;
tab0=[];
tab0.append(" ");
for i in range (len(op_list)):
     tab0.append(op_list[i]);
#print(tab0);
i=0;
table=[];
table.append(tab0);
for i in range (len(op_list)):
     tab=[];
     j=0;
     row=op_list[i];
     row_order=order_list[i];
     row_lr=lr_list[i];
     tab.append(op_list[i]);
     for j in range(len(op_list)):
          if(row=='(' and op_list[j]==')'):
               tab.append('<');
          elif(row=='(' and ( op_list[j]=='$')):
               tab.append('-');
          elif(row==')' and (op_list[j]=='i' or op_list[j]=='(')):
               tab.append('-');
          elif(row=='i' and op_list[j]=='('):
               tab.append('-');
          elif(row=='$' and op_list[j]==')'):
               tab.append('-');
          elif(op_list[j]==')'):
               tab.append('>');
          elif(op_list[j]=='('):
               tab.append('<');               
          elif(row_order<order_list[j]):
               tab.append('>');
          elif(row_order>order_list[j]):
               tab.append('<');
          else:
               if(row_lr=='l' and lr_list[j]=='l'):
                    tab.append('>');
               elif(row_lr=='r'  and lr_list[j]=='r'):
                    tab.append('<');
               else:
                    tab.append('-')
               

     #print(tab);
     table.append(tab);
          

#printing table to precedence_table         
i=0;
file=open('table.txt','w');
print("Precedence Table");
file.write("Precedence Table"+'\n');
line="-----";
temp=table[0];
temp_str="";
line=line+"-----";
line=line+"-----";
line=line+"-----";

for i in range(len(temp)):
     line=line+"-----";
     
     temp_str=temp_str+temp[i];
     temp_str=temp_str+"      ";
file.write(line+'\n');
print(line);     
print(temp_str);
print(line);
file.write(temp_str+'\n');
file.write(line+'\n');

for i in range (1,len(table)):
     temp_list=table[i];
     temp_str="";
     for j in range(len(temp_list)):
      temp_str=temp_str+temp_list[j];
      temp_str=temp_str+"      ";
     print(temp_str);
     file.write(temp_str+'\n');
     print(line);
     file.write(line+'\n');

file.close();
#-------------------------------------------------------
'''i=0;
j=0;
for i in range(len(table)):
     for j in range(len(table[i])):
          print(table[i][j],end =" ")
     print("");  '''   

#-------------------------------------------------------
print("Enter String:");
inp=input();
#print(inp);
#print(op_list);
#checking for valid input
'''for i in range(len(inp)-1):
     if((inp[i]!='i'and inp[i+1]!='i' and (inp[i] in op_list) and (inp[i+1] in op_list))or(inp[i+1]=='i' and inp[i]=='i')):
          print(inp[i]+','+inp[i+1]);
          print('ERROR');
          break;'''

stack='';
stack+='$';
i=0;
inp=inp+'$';

#checking of production
'''
#condition1
i=0;
for i in range(len(inp)-1):
     if((inp[i] in op_list and inp[i+1] in op_list))
'''   
count=1;
while (not(inp=='$' and len(stack)==2 and stack[1]=='E' and stack[0]=='$')) :
     #x=stack[-1];
     #print(count);
     count+=1;
     i=0;


     x=findx(stack,op_list);
     y=inp[0];
     #print('y is'+y);
     index1=op_list.index(x)+1;
     index2=op_list.index(y)+1;
     
     action=table[index1][index2];
     #print(action);
     if(action=='<'):
          
          stack+=inp[0];
          
          
          inp=inp[1:];
          #print('inp is'+inp);
          print(stack+' '+inp+' shift');
     elif(action=='>'):
          
          stack=reduce(stack,pro_matrix);
          if(stack=='ERROR'):
               print('Error');
               break;
          else:
           print(stack+' '+inp+' reduce');
          
          #break;
     else:
          print("ERROR");
          break;
          
     


