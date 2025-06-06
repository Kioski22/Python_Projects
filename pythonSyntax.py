# print("Hello")  print('world') this doesnt work because python doesnt know where the new line or statement starts or end
#how to fix this? simply by adding semicolon ; 

print("Hello") ; print('world')

#or make it a new line

print('Hello')
print('world')

# whitespaces around math operators
 
x = 1                                            +               2
print(x) 

#this works fine  because python ignores extra spaces just like this comment 


#breaking Math into two lines 
y= 1+2
+3
print(y)
 
 #it doesnt work the way you would totaly expect. The second line +3 is treated like seperate code and gets ignored.
 # to fix this you  can use a back slash to continue the line 
 
z=1+2\
+3
print(z) # now this prints 6 
# Why? Because the backslash tells Python: “Hey, this line continues below!”


# now indentation 

name = 'Randy'

if name =='Randy': # if name(a variable) contains the data 'Randy'
    name = "nicole"# change the data of name(the variable) to nicole
    print(name) # and print the name variable 
# this works and it prints nicole
# The line under if must be indented (moved a bit to the right).

# if You Remove the Indentation:

# if name == "John":
# print(name)

 
#❌ You get an error: IndentationError
#Why? Python expects the block under if to be indented. No indentation = Python gets confused. 

"""
    Summary in Simple Terms
--Python is picky about how your code looks.

--Extra spaces within a line are usually okay, but where you put new lines or indents really matters.

--Use new lines or semicolons to separate commands.

--Use a backslash \ if your code continues on the next line.

--Always indent code properly, especially after if, for, while, etc.

--If something goes wrong, read the error message—it usually tells you what’s wrong and where.

"""