full_word = "AAAAAAAAAAAAAAAAAAAABBBBBBBBCCCCCCCCCDDDDDDDDDDDDDDDDDDDEEEEEEEEEFFFFFFFFFFFFFFFFFFFGHHHHHHHHHHHHHHHHHHHIIIIIJJJKKKKKKKKKKKKKKKKKKLLLLLMMMMMMMMMMMMMMMMMMMMNNNNNNNNNNNNNOOOOOPPPPPPPPPPPPPPPPPPPQQQQQQQQQQQQQQQQQQQRSSSSSSSTTTTTUUUUUUUUUUUUUUVVVVVVVVVVVVVVVWWWWWWWWWWWWWWWWWWWWWWWXXXXXXXXXXXXXXXXXXXXXXXXXYYYYYYYYYYYYYYYZZZZZZZZZZZZZZZZZZZZZAAAAAAAAAAABBBBBBBBBBBBBBCCCCCCCCCCCCCCCDDDDDDDDDDDDDDDDDDDDDDDEEEEEEEEEEEEEEEEEEEEEEEFFFFFFFFGHHHHHHHHHHHHHHHHHHHHIIIIIIIIIIIIIIIIIIIIIIIJKKKKKKKKKKKKKKKKKKKLLLLMMMMMMMMMMMMMMMNNNNNNNNNNNNNNOOOOOPPPPPPPPPPPPPPPPPPPPQQQQQQQQQQQQQQQRRRSSSSSSSSSSSSSSSSSSTTTTTUVVVVVVVVVVVVVVVVVVVVWWWWWXXXXXXXXXYYYYYYYYYYYYYYYYYYYYZZZZZAAAAAAAAAAAAAABBBCCCCCCCCCCCCCCCDDDDEEEEEFFFFFFFFFFFFFFFFFFFFFFFFFGGGGGGGGGGGGGGGHHHHHHHHHHHHHHHHHHHHHIIIIIIIIIIIIIIIIIIJJJJJJJJJJJJJJKLLLLLLLLLLLLLMMMMMNNNNNNOOOOOOOOOPPPPPPPPPPPPPPPPPPQQQQQQQQQQQQQQQQQQQRRRRRRRRRRRRRRRRRRRRSTTTTTTTTTTTTTTUUUUVVVVVVVVVVVVWXXXXXXXXXXXXXXXXXXXYYYYYYYYYYYYYYYYYYYYZZZZZZZZZZZZZZZZZZZZZAAAAAAAAAAAAAAAAAAABBBBBBBBBCCCCCCCCCCCCCCDDDDDDDEEEEEEEEEEEEEEEEEEEEFFFFFFFFGGGGGHHHHHHHHHHHHHHHHHHHIJJJJJJJJJJJJJKKKKKLLLLLLLLLLLLLMMMMMNNNNNNNNNNNNNNNNNNNNOOOOOOOOPPPPPPPPPPPPPPPQQQQRSSSSSSSSSSSSSSTTTTUUUUUUUUUUUUUUUUUUUVVVVVVVVVVVVVVVVVVVVVWWXXXXXXXXXXXXXYYYYYYYYYZZZZZZZZZZZZZZZZZZZZAAAAAAAAABBBBBBBBBBBBBBBBBBBBCDDDDDDDDDDDDDDDDDDDEEEEEEEEEEEEEEEEEEEEEEEEEFFFFFFFFFFFFFFFGGGGGGGGGGGGGGGGGGGGGHHHHHHHHHHHHHHHHHHIIIIIIIIIIIIIIIIIIJJJJJKKKKKKKKKKKKKKKKKKKLLLLLLLLLLLLLLLLMMMMMMMMMMMMMMMNNNNNNNNNNNNNNOOOOOOOOOOOOOOOOOOOPPPPP"

def decode(word):
    result = ""
    count = 1
    for i in range(1, len(word)):
        if word[i] == word[i-1] and i != len(word)-1:
            count += 1
        else:
            if i == len(word)-1:
                count += 1
            result += chr(ord("A")-1+count)
            count = 1
    return result
            
def encode(word):
    result = ""
    let = ord("A")
    for char in word:
        result += chr(let) * (ord(char)-(ord("A")-1))
        let += 1
    return result

print(decode(full_word))
print(encode("CARLOSDOBLE"))

