import json
import os
def load_notes():
    try:
        if os.path.exists("notes.json"):
            with open("notes.json", "r") as f:
                return json.load(f)
    except:
        pass
    return []

def save_notes(notes):
    with open("notes.json", "w") as f:
        json.dump(notes, f, indent=2)

def create_note(notes):
    print("\n--- Create Note ---")
    title = input("Title: ")
    content = input("Content: ")
    note = {
        "id": len(notes) + 1,
        "title": title,
        "content": content
    }
    notes.append(note)
    save_notes(notes)
    print("Note created successfully!")

def view_notes(notes):
    if not notes:
        print("\nNo notes available!")
        return
    print("\n--- All Notes ---")
    for note in notes:
        print(f"\nID: {note['id']}")
        print(f"Title: {note['title']}")
        print(f"Content: {note['content']}")
        print("---")

def search_notes(notes):
    keyword = input("\nEnter search keyword: ").lower()
    found = []
    for note in notes:
        if keyword in note["title"].lower() or keyword in note["content"].lower():
            found.append(note)
    
    if not found:
        print("No notes found!")
        return
    
    print("\n--- Search Results ---")
    for note in found:
        print(f"\nID: {note['id']}")
        print(f"Title: {note['title']}")
        print(f"Content: {note['content']}")
        print("---")

def edit_note(notes):
    if not notes:
        print("\nNo notes to edit!")
        return
    
    try:
        note_id = int(input("\nEnter note ID to edit: "))
        for note in notes:
            if note["id"] == note_id:
                print(f"Current title: {note['title']}")
                note["title"] = input("New title: ")
                print(f"Current content: {note['content']}")
                note["content"] = input("New content: ")
                save_notes(notes)
                print("Note updated successfully!")
                return
        print("Note ID not found!")
    except ValueError:
        print("Invalid ID!")

def delete_note(notes):
    if not notes:
        print("\nNo notes to delete!")
        return
    
    try:
        note_id = int(input("\nEnter note ID to delete: "))
        for i in range(len(notes)):
            if notes[i]["id"] == note_id:
                deleted = notes.pop(i)
                save_notes(notes)
                print(f"Note '{deleted['title']}' deleted!")
                return
        print("Note ID not found!")
    except ValueError:
        print("Invalid ID!")

def main():
    notes = load_notes()
    
    while True:
        print("\n" + "="*40)
        print("PERSONAL KNOWLEDGE VAULT")
        print("="*40)
        print("1. Create Note")
        print("2. View All Notes")
        print("3. Search Notes")
        print("4. Edit Note")
        print("5. Delete Note")
        print("6. Exit")
        print("="*40)
        
        choice = input("\nEnter your choice (1-6): ")
        
        if choice == "1":
            create_note(notes)
        elif choice == "2":
            view_notes(notes)
        elif choice == "3":
            search_notes(notes)
        elif choice == "4":
            edit_note(notes)
        elif choice == "5":
            delete_note(notes)
        elif choice == "6":
            print("\nThank you for using Knowledge Vault!")
            break
        else:
            print("\nInvalid choice! Please enter 1-6.")

if __name__ == "__main__":
    main()