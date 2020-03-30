def count_palindrome(word):
    top_count = len(word)
    for mid in range(1, len(word) - 1):
        count = 0
        low = mid - 1
        high = mid + 1
        while (low >= 0 and high < len(word) and word[low-1] == word[high+1]):
            count += 1
            low -= 1
            high += 1
        
        top_count += count
        count = 0

        low = mid - 1
        high = mid

        while (low >= 0 and high < len(word) and word[low-1] == word[high+1]):
            count += 1
            low -= 1
            high += 1
        
        top_count += count
    
    return top_count

def main():
    word = input("Enter a word to check the number of pallindromes: ")
    count_palindrome(word)

main()