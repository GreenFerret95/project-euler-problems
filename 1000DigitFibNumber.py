from email import utils
import Utils

should_run = True
fib = [1, 1]
i = 2
while(should_run):
    fib.append(fib[i-2]+fib[i-1])
    digit_length = len(list(str(fib[len(fib)-1])))
    if(digit_length == 1000):
        print(f'{len(fib)}\n\ndigit_length={digit_length}')        
        should_run = False
    else:
        i += 1