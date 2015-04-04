def main(num):
    strnum = str(num)
    palindrome = True
    for x in range(0, len(strnum)):
        if strnum[x] != strnum[-x-1]:
            palindrome = False
    return palindrome