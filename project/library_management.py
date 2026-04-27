from datetime import date, datetime, timedelta

#-----------------------------------------------
books_file = "books.txt"
members_file = "members.txt"
issued_file = "issued.txt"
history_file = "history.txt"

class BookManager:
    def __init__(self):
        self.books = {}
        self._counter = 1
        self.load()

    def load(self):
        with open(books_file, "a+") as f:
            f.seek(0)
            for line in f:
                parts = line.strip().split("|")
                if len(parts) != 5:
                    continue
                id, title, author, copies, available = parts

                self.books[id] = {
                    "id" : id, "title": title, "author": author,  "copies": int(copies), "available": int(available)
                }   
                num = int(id[1:])
                if num >= self._counter:
                  self._counter = num + 1 
    
    
    def _save(self):
        with open(books_file, "w") as f:
         for b in self.books.values():
            f.write(f"{b['id']}|{b['title']}|{b['author']}|{b['copies']}|{b['available']}\n")

    def _next_id(self):
        b_id = f"B{self._counter:03d}"
        self._counter += 1
        return b_id

    def get_book(self, book_id):
        return self.books.get(book_id)

    def is_available(self, book_id):
        b = self.get_book(book_id) 
        return b and b["available"] > 0

    def reduce_availability(self, book_id):
        self.books[book_id]["available"] -= 1
        self._save()
        

    def increase_availability(self, book_id):
        self.books[book_id]["available"] += 1
        self._save()

    def add_book(self):
        print("\n--- Add New Book ---")
        title = input("Title  : ").strip()
        author = input("Author  : ").strip()

        try:
            copies = int(input("Number of copies: ").strip())
        except ValueError:
            copies = 1

        if not title or not author:
            print("Title and Author are required.")
            return

        b_id  = self._next_id()

        self.books[b_id] = {
            "id":       b_id,
            "title":    title,
            "author":    author,
            "copies":   copies,
            "available": copies
        }         
        self._save()
        print(f"\n✔ Book added with ID: {b_id}")

    def remove_book(self):
        self.list_books()
        b_id = input("\nEnter book id to remove: ").strip().upper()    

        if b_id not in self.books:
            print("Book ID not found!")
            return
        if self.books[b_id]["available"] != self.books[b_id]["copies"]:
            print("cannot remove - some copies are currently issued.")
            return
        
        confirm = input(f"Remove '{self.books[b_id]['title']}'? (y/n): ").strip().lower()

        if confirm == "y":
            del self.books[b_id]
            self._save()
            print("✔ Book removed.")

    def list_books(self):
        print("\n--- Book List ---")
        if not  self.books:
            print("No books in the library.")
            return
        
        print(f"{'ID':<8} {'Title':<30} {'Author':<20}  {'Avail/Total'}")

        print("-" * 80)

        for b in self.books.values():
            print(f"{b['id']:<8} {b['title']:<30} {b['author']:<20}  {b['available']}/{b['copies']}")



class MemberManager:
    def __init__(self):
        self.members = {}
       # member_id: {name, phone, email, address, status}
        self._counter = 1
        self.load()

    
    def load(self):
        with open(members_file, "a+") as f:
            f.seek(0)

            for line in f:
                parts = line.strip().split("|")
                if len(parts) != 6:
                    continue
                id, name, phone, email, address, status = parts

                self.members[id] = {
                    "id": id, "name": name, "phone": phone, "email": email,
                    "address": address, "status": status
                }
                num = int(id[1:])
                if num >= self._counter:
                    self._counter = num + 1


    def _save(self):
        with open(members_file, "w") as f:
            for m in self.members.values():
                f.write(f"{m['id']}|{m['name']}|{m['phone']}|{m['email']}|{m['address']}|{m['status']}\n")                

    def _next_id(self):
        mid = f"M{self._counter:03d}"
        self._counter += 1
        return mid

    def get_member(self, member_id):
        return self.members.get(member_id)

    def is_active(self, member_id):
        m = self.get_member(member_id)
        return m and m["status"] == "Active"

    def cancel_membership(self, member_id):
        if member_id in self.members:
            self.members[member_id]["status"] = "Cancelled"
            self._save()
    
    def add_member(self):
        print("\n--- Register New Member ---")
        name    = input("Full Name : ").strip()
        phone   = input("Phone     : ").strip()
        email   = input("Email     : ").strip()
        address = input("Address   : ").strip()

        if not name or not phone:
            print("Name and phone are required.")
            return

        mid = self._next_id()
        self.members[mid] = {
            "id":      mid,
            "name":    name,
            "phone":   phone,
            "email":   email,
            "address": address,
            "status":  "Active"
        }
        self._save()
        print(f"\n✔ Member registered with ID: {mid}")

    def remove_member(self):
        self.view_members()
        mid = input("\nEnter Member ID to remove: ").strip().upper()

        if mid not in self.members:
            print("Member ID not found.")
            return
        
        confirm = input(f"Remove '{self.members[mid]['name']}'? (y/n): ").strip().lower()

        if confirm == "y":
            del self.members[mid]
            self._save()
            print("✔ Member removed.")

    def view_members(self):

        print("\n--- Member List ---")

        if not self.members:
            print("No members registered.")
            return
        
        print(f"{'ID':<8} {'Name':<25} {'Phone':<15} {'Email':<25} {'Status'}")
        print("-" * 85)

        for m in self.members.values():
            print(f"{m['id']:<8} {m['name']:<25} {m['phone']:<15} {m['email']:<25} {m['status']}")



DATE_FMT = "%Y-%m-%d"
LOAN_DAYS = 14 #default loan period

def parse_date(d):
    return datetime.strptime(d, DATE_FMT).date()

def today_str():
    return date.today().strftime(DATE_FMT)

def calculate_fine(due_date_str, return_date_str):

    due = parse_date(due_date_str)
    ret = parse_date(return_date_str)
    diff = (ret - due).days # neagtive or zero means on time

    if diff <= 0:
        return 0, 0.0, False
    
    days_late = diff
    cancelled =  days_late > 30

    if cancelled:
        return days_late, 0.0, True
    fine = 0.0

    if days_late <= 5:
        fine = days_late * 0.50
    elif days_late <= 10:
        fine = 5 * 0.50 + (days_late - 5) * 1.00
    else:
        fine = 5 * 0.50 + 5 * 1.00 + (days_late - 10) * 5.00

    return days_late, fine, False


class IssueManager:
    def __init__(self, book_manager, member_manager):

        self.bm       = book_manager
        self.mm       = member_manager
        self.issued   = {} #active issues
        self.history  = [] #return record
        self._counter = 1
        self.load()


    def load(self):
        with open(issued_file, "a+") as f:
            f.seek(0)

            for line in f:
                parts = line.strip().split("|")
                if len(parts) != 7:
                    continue
                id, book_id, book_title, member_id, member_name, issue_date, due_date = parts

                self.issued[id] = {
                    "id": id,
                    "book_id": book_id,
                    "book_title": book_title,
                    "member_id": member_id,
                    "member_name": member_name,
                    "issue_date": issue_date,
                    "due_date": due_date
                }
                num = int(id[1:])
                if num >= self._counter:
                    self._counter = num + 1

        with open(history_file, "a+") as f:
            f.seek(0)
            for line in f:
                parts = line.strip().split("|")
                if len(parts) != 11:
                    continue
                id, book_id, book_title, member_id, member_name, issue_date, due_date, return_date, days_late, fine, cancelled = parts

                self.history.append({
                    "id": id,
                    "book_id": book_id,
                    "book_title": book_title,
                    "member_id": member_id,
                    "member_name": member_name,
                    "issue_date": issue_date,
                    "due_date": due_date,
                    "return_date": return_date,
                    "days_late": int(days_late),
                    "fine": float(fine),
                    "cancelled": cancelled == "True"
                })

    def _save(self):
        with open(issued_file, "w") as f:
            for r in self.issued.values():
                f.write(f"{r['id']}|{r['book_id']}|{r['book_title']}|{r['member_id']}|{r['member_name']}|{r['issue_date']}|{r['due_date']}\n")

    def _save_history(self):
        with open(history_file, "a+") as f:
            f.seek(0)

            for r in self.history:
                f.write(f"{r['id']}|{r['book_id']}|{r['book_title']}|{r['member_id']}|{r['member_name']}|{r['issue_date']}|{r['due_date']}|{r['return_date']}|{r['days_late']}|{r['fine']}|{r['cancelled']}\n")                         

    def _next_id(self):
        iid = f"I{self._counter:04d}"
        self._counter += 1
        return iid

    def _list_active(self):

        if not self.issued:
            print("No books are currently issued.")
            return
        
        print(f"\n{'Issue ID':<10} {'Book':<28} {'Member':<20} {'Issue Date':<12} {'Due Date':<12} {'Status'}")
        print("-" * 95)

        today = date.today()

        for rec in self.issued.values():
            due   = parse_date(rec["due_date"])
            late  = (today - due).days

            status = f"OVERDUE {late}d" if late > 0 else "Active"

            print(f"{rec['id']:<10} {rec['book_title']:<28} {rec['member_name']:<20} "
                  f"{rec['issue_date']:<12} {rec['due_date']:<12} {status}")
    
    def issue_book(self):
        
        print("\n--- Issue Book ---")
        self.mm.view_members()
        mid = input("\nEnter Member ID: ").strip().upper()

        if not self.mm.get_member(mid):
            print("Member not found.")
            return
        if not self.mm.is_active(mid):
            print("Member is not active (membership may be cancelled).")
            return

        self.bm.list_books()
        bid = input("\nEnter Book ID: ").strip().upper()

        if not self.bm.get_book(bid):
            print("Book not found.")
            return
        if not self.bm.is_available(bid):
            print("No copies available for this book.")
            return

        issue_date = today_str()
        due_date   = (date.today() + timedelta(days=LOAN_DAYS)).strftime(DATE_FMT)

        iid = self._next_id()
        member = self.mm.get_member(mid)
        book   = self.bm.get_book(bid)

        self.issued[iid] = {
            "id":           iid,
            "book_id":      bid,
            "book_title":   book["title"],
            "member_id":    mid,
            "member_name":  member["name"],
            "issue_date":   issue_date,
            "due_date":     due_date
        }

        self.bm.reduce_availability(bid)
        self._save()
        print(f"\n✔ '{book['title']}' issued to {member['name']}")
        print(f"  Issue ID : {iid}")
        print(f"  Due Date : {due_date}")

    def return_book(self):
        print("\n--- Return Book & Calculate Fine ---")
        self._list_active()
        self._save_history()

        if not self.issued:
            return

        iid = input("\nEnter Issue ID: ").strip().upper()
        if iid not in self.issued:
            print("Issue ID not found.")
            return

        rec         = self.issued[iid]
        return_date = input(f"Return date (YYYY-MM-DD) [default today {today_str()}]: ").strip()
        if not return_date:
            return_date = today_str()

        # Validate date format
        try:
            parse_date(return_date)
        except ValueError:
            print("Invalid date format.")
            return

        days_late, fine, cancelled = calculate_fine(rec["due_date"], return_date)

        print("\n" + "=" * 45)
        print(f"  Book   : {rec['book_title']}")
        print(f"  Member : {rec['member_name']}")
        print(f"  Due    : {rec['due_date']}")
        print(f"  Return : {return_date}")
        print("-" * 45)

        if days_late <= 0:
            print("  Returned on time. No fine.")
        elif cancelled:
            print(f"  Days Late : {days_late}")
            print("  FINE      : Membership will be CANCELLED")
            print("             (returned more than 30 days late)")
        else:
            print(f"  Days Late : {days_late}")
            print(f"  Fine      : Rs {fine:.2f}")
            print("=" * 45)

        confirm = input("\nConfirm return? (y/n): ").strip().lower()

        if confirm != "y":
            print("Return cancelled.")
            return

        # Update records
        self.bm.increase_availability(rec["book_id"])
        if cancelled:
            self.mm.cancel_membership(rec["member_id"])
            print(f"\n⚠ Membership of {rec['member_name']} has been CANCELLED.")
        else:
            print(f"\n✔ Book returned successfully. Fine collected: Rs {fine:.2f}")

        # Move to history
        history_rec = {**rec, "return_date": return_date, "days_late": days_late,
                       "fine": fine, "cancelled": cancelled}
        
        self.history.append(history_rec)
        del self.issued[iid]
        self._save()

class Reports:
     
    def __init__(self, book_manager, member_manager, issue_manager):
        self.bm = book_manager
        self.mm = member_manager
        self.im = issue_manager

    def show_reports(self):
        while True:
            print("\n--- Reports ---")
            print("  1. Fine Report")
            print("  2. Book Status Report")
            print("  3. Member Details Report")
            print("  4. Overdue Books Report")
            print("  0. Back")
            choice = input("Enter choice: ").strip()
            if choice == "1":
                self.fine_report()
            elif choice == "2":
                self.book_status_report()
            elif choice == "3":
                self.member_report()
            elif choice == "4":
                self.overdue_report()
            elif choice == "0":
                break
            else:
                print("Invalid choice.")

    def fine_report(self):
        print("\n=== Fine Report ===")
        history = self.im.history
        if not history:
            print("No returns on record.")
            return

        fines = [r for r in history if r["fine"] > 0 or r["cancelled"]]
        if not fines:
            print("No fines have been levied.")
            return

        total = 0.0
        print(f"\n{'Member':<22} {'Book':<28} {'Days Late':<12} {'Fine (Rs)':<12} {'Return Date'}")
        print("-" * 90)
        for r in fines:
            fine_str = "CANCELLED" if r["cancelled"] else f"{r['fine']:.2f}"
            print(f"{r['member_name']:<22} {r['book_title']:<28} {r['days_late']:<12} {fine_str:<12} {r['return_date']}")
            if not r["cancelled"]:
                total += r["fine"]
        print("-" * 90)
        print(f"{'Total Fines Collected:':<54} Rs {total:.2f}")

    def book_status_report(self):
        print("\n=== Book Status Report ===")
        books = self.bm.books
        if not books:
            print("No books in the library.")
            return
        print(f"\n{'ID':<8} {'Title':<30} {'Author':<20} {'Available':<10} {'Total'}")
        print("-" * 90)
        for b in books.values():
            status = "All Issued" if b["available"] == 0 else str(b["available"])
            print(f"{b['id']:<8} {b['title']:<30} {b['author']:<20}  {status:<10} {b['copies']}")

    def member_report(self):
        print("\n=== Member Details Report ===")
        members = self.mm.members
        if not members:
            print("No members registered.")
            return
        print(f"\n{'ID':<8} {'Name':<25} {'Phone':<15} {'Email':<25} {'Status'}")
        print("-" * 85)
        for m in members.values():
            print(f"{m['id']:<8} {m['name']:<25} {m['phone']:<15} {m['email']:<25} {m['status']}")

    def overdue_report(self):
        print("\n=== Overdue Books Report ===")
        issued = self.im.issued
        today  = date.today()
        overdue = [
            r for r in issued.values()
            if (today - parse_date(r["due_date"])).days > 0
        ]
        if not overdue:
            print("No overdue books. All good!")
            return
        print(f"\n{'Issue ID':<10} {'Book':<28} {'Member':<20} {'Due Date':<12} {'Days Late'}")
        print("-" * 80)
        for r in overdue:
            days_late = (today - parse_date(r["due_date"])).days
            print(f"{r['id']:<10} {r['book_title']:<28} {r['member_name']:<20} {r['due_date']:<12} {days_late}")





def print_header(title):
    print("\n" + "=" * 50)
    print(f" {title}")
    print("=" * 50)


def main_menu():
    
    print_header("Library Management System")
    print("  1. Book Management")
    print("  2. Member Management")
    print("  3. Issue Book")
    print("  4. Return Book")
    print("  5. Report")
    print("  0. Exit")
    print("-" * 50)

    return input("Enter Choice: ").strip()

def book_menu(bm):
    while True:

        print_header("BOOK MANAGEMENT")
        print("  1. Add Book")
        print("  2. Remove Book")
        print("  3. List All Books")
        print("  0. Back")
        
        choice = input("Enter Choice: ")
        if choice == "1":
            bm.add_book()
        elif choice == "2":
            bm.remove_book()
        elif choice == "3":
            bm.list_books()
        elif choice == "0":
            break
        else:
            print("Invalid Choice")            

def member_menu(mm):
    while True:
        print_header("MEMBER MANAGEMENT")
        print("  1. Add Member")
        print("  2. Remove Member")
        print("  3. View Member")
        print("  0. Back")

        choice = input("Enter Choice: ").strip()
        if choice == "1":
            mm.add_member()
        elif choice == "2":
            mm.remove_member()
        elif choice == "3":
            mm.view_members()
        elif choice == "0":
            break
        else:
            print("Invalid choice.")

def main():
    bm = BookManager()
    mm = MemberManager()
    im = IssueManager(bm, mm)
    rp = Reports(bm, mm, im)
    
    while True:
         choice = main_menu()

         if choice == "1":
             book_menu(bm)
         elif choice == "2":
            member_menu(mm)
         elif choice == "3":
            im.issue_book()
         elif choice == "4":
            im.return_book()
         elif choice == "5":
            rp.show_reports()

         elif choice == "0":
            print ("\n Thank you for using Library Management system. Have A Good Day!")
            break
         else:
            print("Invalid Choice. Try Again.")                    


if __name__ == "__main__":
        main()
       
