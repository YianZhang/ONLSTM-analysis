import random
random.seed(54312)

def randomize_split(sentence):
    if len(sentence) == 2:
        return sentence
    elif len(sentence) == 1:
        return sentence[0]
    else:
        split = random.choice(list(range(len(sentence)-1)))+1
        return [randomize_split(sentence[:split]),randomize_split(sentence[split:])]

def parenthesize(l):
    if isinstance(l,str):
        return '(<word> '+l+')'
    else:
        return f'(<unk> {parenthesize(l[0])} {parenthesize(l[1])})'
	
for i in range(5):
	with open('wsjtest_sample.txt','r') as f_in:
		with open('wsjtest_random_baseline'+str(i),'w') as f_out:
			for line in f_in:
				f_out.write(parenthesize(randomize_split(line.rstrip('\n').split())).lower()+'\n')
	with open('wsj10_sample.txt','r') as f_in:
		with open('wsj10_random_baseline'+str(i),'w') as f_out:
			for line in f_in:
				f_out.write(parenthesize(randomize_split(line.rstrip('\n').split())).lower()+'\n')
				
