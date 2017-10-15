#!/usr/bin/env
'''
Udemy's The Complete Python Bootcamp
Project 1 - Tic Tac Toe
'''
from __future__ import print_function


# GLOBAL VARIABLES
BOARD_SIZE = 9
BOARD = [' '] * BOARD_SIZE

VALID_PLAYER_TYPES = ['X', 'O']
PLAYER_TRACKER = {'X': 0, 'O': 0}
WIN_POSITIONS = [
				(0, 1, 2), (3, 4, 5), (6, 7, 8),
				(0, 3, 6), (1, 4, 7), (2, 5, 8),
				(0, 4, 8)
]


def display_board():
	'''display board'''
	print()
	i = 0
	while i < BOARD_SIZE:
		row = 0
		while row < 3:
			print(BOARD[i], end=' ')
			if row < 2:
				print('|', end=' ')
			row += 1
			i += 1
		if i < BOARD_SIZE - 1:
			print('\n----------')
	print('\n')


def setup():
	'''setup game'''

	while True:
		player = raw_input('Do you want to play as X or O? ')
		player = player.upper()

		if player not in VALID_PLAYER_TYPES:
			print('ERROR: You can only play as X or O!')
		else:
			break

	player_type = VALID_PLAYER_TYPES.index(player)
	return player_type


def check_if_player_won(player):
	'''check if player won'''
	#print("Checking {}'s status...".format(player))
	player_positions = [i for i, x in enumerate(BOARD) if x == player]
	#print('Player positions:', player_positions)
	for position in WIN_POSITIONS:
		#print('\tComparing {} with {}'.format(position, player_positions))
		#print(set(position), set(player_positions))
		player_won = set(position) <= set(player_positions)
		#print('Player won?', player_won)
		if player_won:
			print('Congratulations! Player {} won!'.format(player))
			return True

	return False


def check_win_status():
	'''check for win status'''
	win_status = False
	#print(PLAYER_TRACKER.values())
	for player in PLAYER_TRACKER:
		#print(PLAYER_TRACKER[player])
		if PLAYER_TRACKER[player] >= 3:
			win_status = check_if_player_won(player)
			if win_status:
				break
	return win_status


def check_draw_status():
	'''check if there is a draw'''
	blank_boxes = [i for i in BOARD if i == ' ']
	return len(blank_boxes) == 0


def check_game_end():
	'''check if game is finished'''
	# check for win status
	win_status = check_win_status()

	# check for draw status
	draw_status = check_draw_status()
	if draw_status:
		print('Game ended with a draw!')
	#print('game status', win_status | draw_status)
	return win_status | draw_status


def get_next_position(player_type):
	'''gets player's next position'''
	while True:
		position = raw_input('Where do you want to place? ')
		#print(position, type(position))
		position = int(position)

		#if not isinstance(position, int):
		#	print('ERROR: Enter a value between 0 and {}'.format(BOARD_SIZE - 1))
		if position not in range(BOARD_SIZE):
			print('ERROR: You can only pick a position up to {}'.format(BOARD_SIZE - 1))
		elif BOARD[position] != ' ':
			print('ERROR: Board already occupied at position {}!'.format(position))
		else:
			break

	#print('\nPlacing {} in position {}'.format(player_type, position))
	PLAYER_TRACKER[VALID_PLAYER_TYPES[player_type]] += 1
	BOARD[position] = VALID_PLAYER_TYPES[player_type]
	player_type ^= 1
	return player_type


def play_tic_tac_toe():
	'''play tic tac toe game'''
	print('Welcome to Tic Tac Toe!')
	display_board()
	player_type = setup()

	is_game_complete = False

	while not is_game_complete:
		print("\nPlayer {}'s turn".format(VALID_PLAYER_TYPES[player_type]))
		player_type = get_next_position(player_type)

		display_board()
		is_game_complete = check_game_end()


def main():
	'''main program'''
	play_tic_tac_toe()
	#display_board()


if __name__ == '__main__':
	main()
	