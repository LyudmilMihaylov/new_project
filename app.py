import sqlite3

# Connect to database (or create it)
conn = sqlite3.connect("notes.db")
cursor = conn.cursor()

# Create table for storing notes
cursor.execute("""
CREATE TABLE IF NOT EXISTS notes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    content TEXT NOT NULL
)
""")
conn.commit()

def add_note():
    """Add a new note to the database."""
    note = input("Enter your note: ")
    cursor.execute("INSERT INTO notes (content) VALUES (?)", (note,))
    conn.commit()
    print("✅ Note saved!")

def view_notes():
    """View all notes."""
    cursor.execute("SELECT * FROM notes")
    notes = cursor.fetchall()
    
    if notes:
        print("\n📒 Your Notes:")
        for note in notes:
            print(f"{note[0]}. {note[1]}")
    else:
        print("⚠️ No notes found.")

def delete_note():
    """Delete a note by ID."""
    view_notes()
    note_id = input("Enter the ID of the note to delete: ")
    
    cursor.execute("DELETE FROM notes WHERE id = ?", (note_id,))
    conn.commit()
    print("🗑️ Note deleted!")

def search_notes():
    """Search for notes by keyword."""
    keyword = input("Enter keyword to search: ")
    cursor.execute("SELECT * FROM notes WHERE content LIKE ?", ('%' + keyword + '%',))
    notes = cursor.fetchall()

    if notes:
        print("\n🔍 Search Results:")
        for note in notes:
            print(f"{note[0]}. {note[1]}")
    else:
        print("⚠️ No matching notes found.")

def edit_note():
    """Edit an existing note."""
    view_notes()
    note_id = input("Enter the ID of the note to edit: ")
    
    cursor.execute("SELECT * FROM notes WHERE id = ?", (note_id,))
    note = cursor.fetchone()
    
    if note:
        new_content = input(f"Enter new content (was: {note[1]}): ")
        cursor.execute("UPDATE notes SET content = ? WHERE id = ?", (new_content, note_id))
        conn.commit()
        print("✏️ Note updated!")
    else:
        print("❌ Note not found.")

def main():
    while True:
        print("\n📌 Simple Notes App")
        print("1️⃣ Add Note")
        print("2️⃣ View Notes")
        print("3️⃣ Edit Note")
        print("4️⃣ Delete Note")
        print("5️⃣ Search Notes")
        print("6️⃣ Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            add_note()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            edit_note()
        elif choice == "4":
            delete_note()
        elif choice == "5":
            search_notes()
        elif choice == "6":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()

# Close the connection when done
conn.close()
