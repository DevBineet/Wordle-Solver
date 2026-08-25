

vowels = "aeiou"

def score_maker(i,k):
    score = (sum(1 for char in k[i] if char.lower() in 'aeiou')) + distinctness_finder(k[i])
    return score
def loadertxt(n):
    f = open(n , "r")
    k = [line.strip() for line in f.readlines()]
    f.close()
    return k

def word_looper(k):
        
        count = len(k)
        target_word_index = 0
        score = -1
        
        for i in range(0,count):
            temp =score_maker(i,k)
            if ( temp > score):
                    score = temp
                    target_word_index = i
                    #print(k[target_word_index] , score)

        return k[target_word_index]
            #if ((sum(1 for char in k[i] if char.lower() in 'aeiou') >= vowels_per_one) and (distinctness_finder(k[i])>= distinct_per_one)):
               # vowels_per_one = sum(1 for char in k[i] if char.lower() in 'aeiou')
                #index_max_vowel = i
               # print("the max vowels word and most dstinct is" , k[index_max_vowel])

def bada_dimag(valid,k):
    #first we will check that if that it is that is validitity + score thing
    #so first we will sort all the validity then sort b score
    valid_seq = [i.lower() for i in valid]

    valid_words = validity_checker_list(valid,k)
    
    return valid_words





def word_picker_main(k):
    global final_word
    final_word = word_looper(k)
    print("The most correct word i think is" ,final_word)
    global validity
    validity = input("Enter the result in string (y = ywllo ,  g = green , b = blac) : ")
    remaining_words = bada_dimag(validity, k)
    return remaining_words


    

def validity_checker_list(valid,lst):
    greens = []
    yellow = []
    black = []
    print(valid)
    for i in range(5):
        if (valid[i]=='g'):
            greens.append([final_word[i],i])
        elif (valid[i] == 'y'):
            yellow.append([final_word[i],i])
        elif (valid[i] == 'b'):
            black.append(final_word[i])
    print(greens)
    print(yellow)
    print(black)
    valid_prepped = []
    temp_valid = []

    gr_len = len(greens)
    print(gr_len)

    for wrd in lst:
        is_valid = True

        for green_iem in greens:
            char = green_iem[0]
            pos = green_iem[1]
            if (wrd[pos] != char):
                is_valid = False
                break

        if is_valid:
            for yellow_item in yellow:
                char = yellow_item[0]
                pos = yellow_item[1]
                if (char not in wrd) or (wrd[pos] ==  char):
                    is_valid = False
                    break

        if is_valid:
            for blac_items in black:
                # how many times this letter is already confirmed (green or yellow) elsewhere
                accounted = sum(1 for g in greens if g[0] == blac_items) + \
                            sum(1 for y in yellow if y[0] == blac_items)
                if wrd.count(blac_items) > accounted:
                    is_valid = False
                    break

        if is_valid:
           valid_prepped.append(wrd)

                        
    return valid_prepped

def distinctness_finder(s):
    l = []
    for i in s:
        l.append(i)

    unique_list = list(set(l))

    distint_count = len(unique_list)

    return distint_count


def main_game_loop():
    candidate_words = loadertxt("words.txt")
    turn = 1

    while True:
        print(f"\n--- TURN {turn} ---")
        print(f"Remaining possible words: {len(candidate_words)}")

        if not candidate_words:
            print("No matching words found in list!")
            break

        candidate_words = word_picker_main(candidate_words)

        if validity.strip().lower() == "ggggg":
            print(f"Congratulations! Found the word '{final_word}' in {turn} turns!")
            break

        turn += 1


main_game_loop()

main_game_loop()

