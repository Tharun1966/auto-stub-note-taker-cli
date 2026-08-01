import argparse

from notes import NoteManager

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='A command-line tool for taking and managing notes.')
    parser.add_argument('command', choices=['add', 'list', 'delete'], help='Action to perform on notes.') 
    parser.add_argument('--note', help='Note content for add command.')
    parser.add_argument('--id', type=int, help='ID of the note to delete.')
    args = parser.parse_args()

    note_manager = NoteManager()
    if args.command == 'add':
        note_manager.add_note(args.note)
    elif args.command == 'list':
        notes = note_manager.get_notes()
        for note in notes:
            print(note)
    elif args.command == 'delete':
        note_manager.delete_note(args.id)