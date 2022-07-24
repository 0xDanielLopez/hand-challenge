# Solution from @0xDanieLopez to https://github.com/jesus-seijas-sp/hand-challenge

f_in="input.hand"
with open(f_in, 'r') as f:
	hand_list = f.read()

cell=[0]
pointer=0
pointer_list=0
result=[]

count_nest=0
count_before=0

while pointer_list < len(hand_list):

	hand=hand_list[pointer_list]

	if hand=="👉":
		pointer=pointer+1

		if pointer >= len(cell):
			cell.append(0)

	elif hand=="👈":
		pointer=pointer-1

	elif hand=="👆":
		cell[pointer]= cell[pointer]+1

		if cell[pointer] > 255:
			cell[pointer]=0

	elif hand=="👇":
		cell[pointer]= cell[pointer]-1

		if cell[pointer] < 0:
			cell[pointer]=255

	elif hand=="🤜":

		#  If the memory cell at the current position is 0, jump just after the corresponding 🤛
		if cell[pointer] == 0:

			count_before=count_nest

			count_nest=count_nest+1

			flag=0

			while flag==0:

				pointer_list=pointer_list+1
				hand=hand_list[pointer_list]

				if hand == "🤜":
					count_nest=count_nest+1

				if hand == "🤛":

					count_nest=count_nest-1

					if count_nest==count_before:
						flag=1						

		else: # Open nest
			count_nest=count_nest+1			

	elif hand=="🤛":
		
		# If the memory cell at the current position is not 0, jump just after the corresponding 🤜
		if cell[pointer] != 0:

			count_before=count_nest

			flag=0

			while flag==0:

				pointer_list=pointer_list-1
				hand=hand_list[pointer_list]

				if hand == "🤛":
					count_nest=count_nest+1

				if hand == "🤜":

					if count_nest==count_before:
						flag=1
					else:
						count_nest=count_nest-1

		else: # Closed Nest
			count_nest=count_nest-1

	elif hand=="👊":
		print(chr(cell[pointer]), end='')

	else: # Another character detected
		pass

	pointer_list=pointer_list+1