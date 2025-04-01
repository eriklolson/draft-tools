#!/usr/bin/env python

import argparse
from modules.big_board_updater import update_big_board
from modules.game_schedule_creator import create_game_schedule

def main():
    parser = argparse.ArgumentParser(description="Draft Tools for Erik's Big Board")
    parser.add_argument('--update-big-board', action='store_true', help="Update player stats on the big board")
    parser.add_argument('--games', type=str, help="Generate game tables for date YYYY-MM-DD")

    args = parser.parse_args()

    if args.update_big_board:
        update_big_board()

    if args.games:
        create_game_schedule(args.games)

if __name__ == "__main__":
    main()
