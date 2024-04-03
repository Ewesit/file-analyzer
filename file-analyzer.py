#open the file for reading

# f = open('test.txt', 'r') if you use this manner ensure you use the f.close() to close file

# print(f.name)
# print(f.mode)
# always remember to close the file
# f.close()

# To avoid having to use f.close() use below context manager.

# with open('test.txt', 'r') as f:
#     pass
# print(f.closed) if you read contents from a closed file you get an error. 
# To avoid the error read contents from file within the context manager, ie before 'pass'
with open('test.txt', 'r') as f:
    f_contents = f.read()
    print(f_contents)
   