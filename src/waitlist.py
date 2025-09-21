class _Node:
    __slots__ = ("name", "next")
    
    def __init__(self, name, next=None):
        self.name = name
        self.next = next

class Waitlist:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def __len__(self):
        """Return number of people on the waitlist."""
        return self._size

    def to_list(self):
        """Return names from head to tail as a Python list."""
        result = []
        current = self.head
        while current:
            result.append(current.name)
            current = current.next
        return result

    def join(self, name):
        """Append name at the tail (O(1))."""
        new_node = _Node(name)
        if self.tail:
            self.tail.next = new_node
        else:
            self.head = new_node
        self.tail = new_node
        self._size += 1

    def find(self, name):
        """Return True if name exists, else False."""
        current = self.head
        while current:
            if current.name == name:
                return True
            current = current.next
        return False

    def cancel(self, name):
        """Remove first occurrence; return True if removed."""
        current = self.head
        prev = None
        while current:
            if current.name == name:
                if prev:  # Removing from middle or tail
                    prev.next = current.next
                else:  # Removing from head
                    self.head = current.next
                if current == self.tail:  # If we removed the tail, update it
                    self.tail = prev
                self._size -= 1
                return True
            prev = current
            current = current.next
        return False

    def bump(self, name):
        """Move first occurrence to the head; return True if moved."""
        if self.head and self.head.name == name:
            return True  # Already at the head, no need to bump
        
        current = self.head
        prev = None
        while current:
            if current.name == name:
                # Unlink the node
                if prev:
                    prev.next = current.next
                if current == self.tail:  # If it's the tail, update the tail
                    self.tail = prev
                
                # Insert at the head
                current.next = self.head
                self.head = current
                return True
            prev = current
            current = current.next
        return False
