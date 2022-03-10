Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def main():
  n=int(input('enter no.:'))
  x=0
  y=1
  z=0
  while(z<=n):
    print(z)
    x=y
    y=z
    z=x+y
if __name__=='__main__':
    main()