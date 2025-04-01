import requests
from bs4 import BeautifulSoup
from modules import joplin

def scrape_tankathon_big_board():
    url = "https://www.tankathon.com/big_board"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'lxml')

    players = []
    for row in soup.select(".player-row"):
        rank = row.select_one(".player-rank")
        name = row.select_one(".player-name")
        position = row.select_one(".player-pos")
        school = row.select_one(".player-team")
        
        if all([rank, name, position, school]):
            players.append({
                'rank': rank.text.strip(),
                'name': name.text.strip(),
                'position': position.text.strip(),
                'school': school.text.strip()
            })

    return players

def find_big_board_note():
    notebooks = joplin.get_notebooks()
    notebook = next(nb for nb in notebooks if nb['title'] == 'Basketball/Draft/2025')
    notes = joplin.get_notes(notebook_id=notebook['id'])
    note = next(nt for nt in notes if nt['title'] == '0.BigBoard')
    return note

def update_big_board():
    print("Scraping Tankathon...")
    players = scrape_tankathon_big_board()
    print(f"Found {len(players)} players on Tankathon Big Board.")

    print("Accessing Joplin note...")
    note = find_big_board_note()

    # Create a new markdown table
    lines = ["| Rank | Name | Position | School |", "|------|------|----------|--------|"]
    for p in players:
        lines.append(f"| {p['rank']} | {p['name']} | {p['position']} | {p['school']} |")
    new_body = "\n".join(lines)

    print("Updating note in Joplin...")
    joplin.update_note(note_id=note['id'], body=new_body)
    print("Big board successfully updated.")
