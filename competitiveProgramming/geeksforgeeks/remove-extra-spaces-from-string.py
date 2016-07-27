"""
Given a string, remove all the extra spaces from the string.
Input: "   Geeks   for Geeks   "
Output: Geeks for Geeks
"""
def solution1(s):
	return ' '.join(s.split())

def solution2(s):

	def l_trim(s):
		l = len(s)
		for i in range(l):
			if s[i]!=" ":
				s = s[i:]
				return s
	
	def r_trim(s):
		l = len(s)
		for i in range(l):
			if s[l-1-i]!=" ":
				s = s[:l-i]
				return s

	s = r_trim( l_trim(s) )
	
	output = ""

	for i in range(len(s)):
		if s[i] != " ":
			output+=s[i]
		elif s[i] == " " and output[len(output)-1]!=" ":
			output+=" "
	
	return output



# print solution1(" Hello  India .  This    is Kunal  Sharma .   ")
# print solution1("Geeks  for Geeks   ")
print solution2(" Geeks  for Geeks   ")
# print solution2(" Hello  India .  This    is Kunal  Sharma .   ")

"""
Extend this to the case where for a comma(,), fullstop(.), exclamation sign(!), and 
question mart(?) there should be no space from preceeding character.
"""
