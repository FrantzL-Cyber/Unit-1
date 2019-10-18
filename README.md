# Unit-1

The files are organized alphabetically and include most of what was completed during the first half of the semester.
The pieces I chose range from the simple, class exercises, individual projects, and collaborative efforts. 
They help to show the growth in complexity over the length of the course and also include interacting with different capabilities of python.

[Unit 1 files](https://github.com/FrantzL-Cyber/Unit-1) - For the list of python files.


```markdown
### Encrypt
Encrypt.py is the work I am most proud of because it was a collaborative effort 
 with Joy, Nick, and Patrick for multiple sections but we solved part 7 and 8 
 independently, as it was extra credit. This involved us having to integrate 
 ideas the others had developed during previous code and was fascinating to 
 compare how we had each solved the issue.

``` python
 #Part 7 
 password = input('enter a password: ') 
  
 nkey = ''.join(sorted(set(password), key=password.index)) 
 print(nkey) 
  
 alphabet =  'abcdefghijklmnopqrstuvwxyz' 
  
 #print(max(nkey)) 
 #one, two = alphabet.split(max(nkey),1) 
 one, two = alphabet.split(nkey[-1], 1) 
  
  
 #print('first section ', one) 
 #print('second section ', two) 
  
  
 for char in nkey: 
     one = one.replace(char,"") 
  
 for char in nkey: 
     two = two.replace(char,"") 
  
 #print('new first ', one) 
 #print('new first ', two) 
  
 fkey = nkey + two + one 
 print(fkey) 
  
 key = fkey 
 ``` 
 
### Weaknesses

The only piece I do not see as demonstrative of my abilities is the FLecesne_Turtle(1).py.
The reason I would remove it from the collection is because I did not feel much inspiration 
in terms of the final drawing so it was much more of a technical exercise along the way 
than an attempt to create something that truly showcased the tool’s potential. 

### Looking Forward

The projects so far have been great at building up different tools to accomplish specific tasks. 
Although all the work reflects abilities that I now pocess the really interesting aspect is how 
those tools can be used to resolve different problems. So on one hand it is very representative 
of my abilities and on the other it does not show how I will be able to use those same tools in 
the future. This is why I really hope to keep up and improve proper commenting and implementing 
additional print functions within the code. These aspects really help me not only to not only 
follow the code but determine other uses for certain functions.   


To return to my profile page [Click Here](https://frantzl-cyber.github.io/FL_portfolio/).
