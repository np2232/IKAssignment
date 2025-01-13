ta = ['avariciously','badly','calculatingly','decently','deceptively','dishonestly','disloyally','ethically','faithfully','hypocritically',
'insincerely','intriguingly','justly','loyally','lustfully','maliciously','materialistically','morally','nobly','perfidiously','pharisaically',
'rapaciously','righteously','sincerely','truthfully','underhandedly','unfaithfully','unreliably','unscrupulously','untruthfully','uprightly','valiantly',
'virtuously', 'vulgarly']

def main():
    adv_total = 0
    total_length = 0
    for i in range(10):
    #files were named 1.txt, 2.txt, 3.txt etc
        filename = str(i+1) + '.txt'
        with open(filename, 'r') as infile:
            text = infile.read()
            text = text.split()
            total_length += len(text)
        for word in text:
            word = word.strip(',.!?;')
            word = word.lower()
            if word in ta:
                adv_total += 1
    print(total_length)
    print(adv_total)
    print(total_length/adv_total)
            
           
if __name__ == '__main__':
    main()          